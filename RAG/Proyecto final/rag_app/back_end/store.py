import uuid
import chromadb
from chromadb.config import Settings

CHROMA_PATH = "chroma"
COLLECTION_NAME = "rag_documents"

_client = None
_collection = None

def _get_client():
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(
            path=CHROMA_PATH,
            settings=Settings(allow_reset=True)
        )
    return _client

def _get_collection() -> chromadb.Collection:
    """Obtiene o crea la colección en ChromaDB (singleton, persistente)."""
    global _collection
    if _collection is None:
        _client = _get_client()
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"},
        )
    return _collection

def add_chunks(embeddings: list[list[float]], chunks: list[str], source: str):
    collection = _get_collection()

    ids = [str(uuid.uuid4()) for _ in chunks]
    metadata = [
        {
            "source": source,
            "chunk_index": i,
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata,
    )

def delete_chunk(source: str):
    collection = _get_collection()
    try:
        collection.delete(where={"source": source})
    except Exception as e:
        # Si la colección estaba vacía o no encuentra registros, continúa
        pass

