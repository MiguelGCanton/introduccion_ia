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

def add_chunks():
    collection = _get_collection()



