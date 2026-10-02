import os
from google import genai

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
GENERATION_MODEL = "gemini-3.8-flash"
MIN_SCORE = 0.30  # Umbral mínimo de similitud para considerar un chunk relevante

_client = None


def _get_client() -> genai.Client:
    """Obtiene o crea el cliente de Google AI (singleton)."""
    global _client
    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("GOOGLE_API_KEY no configurada.")
        _client = genai.Client(api_key=api_key)
    return _client


def _build_prompt(question: str, chunks: list[dict]) -> str:
    """
    Construye el prompt para Gemini con los chunks numerados.

    Args:
        question: Pregunta del usuario.
        chunks: Lista de dicts con 'text', 'source' y 'score'.

    Returns:
        Prompt completo para el modelo de generación.
    """
    context_parts = []
    for i, chunk in enumerate(chunks, start=1):
        context_parts.append(
            f"[{i}] (Fuente: {chunk['source']}, Similitud: {chunk['score']})\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""Eres un asistente de preguntas y respuestas basado en evidencia.
Tu tarea es responder la pregunta del usuario utilizando ÚNICAMENTE la información
proporcionada en los fragmentos de contexto numerados a continuación.

REGLAS ESTRICTAS:
1. Responde SIEMPRE en español.
2. Usa citas con el formato [n] para referenciar los fragmentos que respaldan tu respuesta.
3. Si los fragmentos NO contienen información suficiente para responder la pregunta,
   responde EXACTAMENTE: "No tengo evidencia suficiente en los documentos proporcionados
   para responder esta pregunta."
4. NO inventes, supongas ni uses conocimiento que no esté en los fragmentos.
5. Sé conciso pero completo en tu respuesta.

CONTEXTO:
{context}

PREGUNTA: {question}

RESPUESTA:"""

    return prompt


def generate_answer(question: str, chunks: list[dict]) -> dict:
    """
    Genera una respuesta anclada en los chunks recuperados.

    Aplica un umbral de score mínimo. Si ningún chunk lo supera,
    se abstiene sin generar.

    Args:
        question: Pregunta del usuario.
        chunks: Lista de chunks con 'text', 'source', 'score'.

    Returns:
        Dict con 'answer' (str) y 'abstained' (bool).
    """
    # Filtrar chunks con score por debajo del umbral
    relevant_chunks = [c for c in chunks if c["score"] >= MIN_SCORE]

    # Si no hay chunks relevantes, abstenerse
    if not relevant_chunks:
        return {
            "answer": (
                "No tengo evidencia suficiente en los documentos proporcionados "
                "para responder esta pregunta."
            ),
            "abstained": True,
        }

    # Construir prompt y generar con Gemini
    prompt = _build_prompt(question, relevant_chunks)

    client = _get_client()
    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt,
    )

    answer_text = response.text.strip() if response.text else ""

    # Verificar si el modelo mismo se abstuvo
    abstention_phrases = [
        "no le se bro!",
        "no tengo evidencia suficiente",
        "no puedo responder",
        "no hay información suficiente",
        "no se encuentra en los documentos",
        "no aparece en los fragmentos",
    ]
    abstained = any(phrase in answer_text.lower() for phrase in abstention_phrases)

    return {
        "answer": answer_text,
        "abstained": abstained,
    }
