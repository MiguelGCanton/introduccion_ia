from pydantic import json_schema
import uuid
import chromadb
from chromadb.config import Settings
import json
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

def add_chunks(embeddings: list[list[float]], chunks: list[str], source: str)-> list[str]:
    print(f"num_chunks:{len(chunks)}")
    
    collection = _get_collection()

    ids = [f"source_{source}_{i}" for i in range(len(chunks))]
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
    return ids

def delete_chunk(source: str):
    collection = _get_collection()
    try:
        collection.delete(where={"source": source})
    except Exception as e:
        # Si la colección estaba vacía o no encuentra registros, continúa
        pass

def get_collection_count() -> int:
    """Retorna el número total de chunks indexados."""
    collection = _get_collection()
    return collection.count()

def query_similar(
    query_embedding: list[float],
    top_k: int = 3
) -> list[dict]:
    """
    Busca los chunks más similares a un embedding de pregunta.

    Args:
        query_embedding: Vector de la pregunta (calculado por Google AI).
        top_k: Número de resultados a retornar.

    Returns:
        Lista de dicts con keys: id, text, source, score, chunk_index.
        Ordenados de mayor a menor similitud (menor distancia).
    """
    collection = _get_collection()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    items = []
    if results and results["ids"] and results["ids"][0]:
        for i in range(len(results["ids"][0])):
            distance = results["distances"][0][i] if results["distances"] else 0.0
            # ChromaDB con cosine retorna distancia (0 = idéntico, 2 = opuesto)
            # Convertimos a score de similitud: 1 - distancia
            score = 1.0 - distance

            metadata = results["metadatas"][0][i] if results["metadatas"] else {}

            items.append({
                "id": results["ids"][0][i],
                "text": results["documents"][0][i],
                "source": metadata.get("source", "desconocido"),
                "score": round(score, 4),
                "chunk_index": metadata.get("chunk_index", -1),
            })

    return items

def reset_chromadb():
    global _client
    if not _client:
        _client= _get_client()
    _client.reset()