import os
from google import genai

_client = None

EMBEDDING_MODEL = "gemini-embedding-001"


def _get_client() -> genai.Client:
    """Obtiene o crea el cliente de Google AI (singleton)."""
    global _client
    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GOOGLE_API_KEY no configurada. "
                "Agrégala al archivo .env"
            )
        _client = genai.Client(api_key=api_key)
    return _client


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Genera embeddings para una lista de textos usando Google AI.

    Usa el modelo text-embedding-004 (o el configurado) para todos
    los textos, tanto documentos como preguntas.

    Args:
        texts: Lista de strings a embeber.

    Returns:
        Lista de vectores (list[float]), uno por cada texto de entrada.
    """
    client = _get_client()

    # Procesar en lotes para respetar límites de la API
    BATCH_SIZE = 100
    all_embeddings = []

    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=batch,
        )
        for embedding in response.embeddings:
            all_embeddings.append(embedding.values)
    print(f"number of embedings: {len(all_embeddings)}")
    return all_embeddings
