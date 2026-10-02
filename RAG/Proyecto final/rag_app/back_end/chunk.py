import io
from pypdf import PdfReader


def read_file_content(content_bytes: bytes, filename: str) -> str:
    """
    Lee el contenido de un archivo según su extensión.

    Args:
        content_bytes: Contenido del archivo en bytes.
        filename: Nombre del archivo (para detectar extensión).

    Returns:
        Texto extraído del archivo.

    Raises:
        ValueError: Si la extensión no es soportada.
    """
    lower = filename.lower()

    if lower.endswith(".pdf"):
        return _read_pdf(content_bytes)
    elif lower.endswith((".txt", ".md", ".markdown")):
        return content_bytes.decode("utf-8", errors="replace")
    else:
        raise ValueError(
            f"Formato no soportado: {filename}. "
            "Usa archivos .txt, .md o .pdf"
        )


def _read_pdf(content_bytes: bytes) -> str:
    """Extrae texto de un archivo PDF usando pypdf."""
    reader = PdfReader(io.BytesIO(content_bytes))
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n\n".join(pages)


def chunk_text(
    text: str,
    chunk_size: int = 300,
    overlap: int = 60,
) -> list[str]:
    """
    Divide texto en chunks de tamaño fijo (en palabras) con overlap.

    Args:
        text: Texto completo a dividir.
        chunk_size: Número de palabras por chunk (default 300).
        overlap: Número de palabras de solape entre chunks consecutivos (default 60).

    Returns:
        Lista de strings, cada uno un chunk del texto original.
    """
    words = text.split()

    if not words:
        return []

    # Si el texto es más corto que un chunk, devolver como único chunk
    if len(words) <= chunk_size:
        return [" ".join(words)]

    chunks = []
    start = 0
    step = chunk_size - overlap

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)

        # Si ya cubrimos todo el texto, salir
        if end >= len(words):
            break

        start += step

    return chunks
