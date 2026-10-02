from functools import wraps
import streamlit as st
import httpx
import logging


def handle_api_errors(func):
    """Decorador que captura errores de red y de servidor para llamadas a la API."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except httpx.ConnectError:
            st.error("❌ No se puede conectar a la API. ¿Está corriendo FastAPI en el puerto 8000?")
            log.error("Fallo de conexión al intentar llamar a la API")
            return None
        except httpx.TimeoutException:
            st.error("⏱️ La API tardó demasiado en responder (Timeout).")
            log.error("Timeout esperando respuesta de la API")
            return None
        except Exception as e:
            st.error(f"Error inesperado: {e}")
            log.exception("Error desconocido en la llamada a la API")
            return None
    return wrapper


# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
API_URL = "http://localhost:8000"
TIMEOUT = 120.0  # segundos (embedding + generación pueden tardar)
log = logging.getLogger(__name__)
# ---------------------------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------------------------
@handle_api_errors
def check_api_health() -> dict | None:
    """Verifica si la API está disponible."""

    response = httpx.get(f"{API_URL}/health", timeout=10.0)
    if response.status_code == 200:
        return response.json()
    return None


def ingest_files(files) -> dict | None:
    """Envía archivos a la API para indexarlos."""

    file_list = [
        ("files", (f.name, f.getvalue(), "application/octet-stream"))
        for f in files
    ]
    response = httpx.post(
        f"{API_URL}/ingest",
        files=file_list,
        timeout=TIMEOUT,
    )
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error del servidor: {response.status_code} — {response.text}")
        return None



def query_api(question: str, top_k: int = 3) -> dict | None:
    """Envía una pregunta a la API."""

    response = httpx.post(
        f"{API_URL}/query",
        json={"question": question, "top_k": top_k},
        timeout=TIMEOUT,
    )
    if response.status_code == 200:
        return response.json()
    else:
        detail = response.json().get("detail", response.text)
        st.error(f"Error: {detail}")
        return None

def reset_database():
    response = httpx.get(
        f"{API_URL}/reset",
        timeout=TIMEOUT,
    )
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code} — {response.text}")
        return None


st.set_page_config(
    page_title="Video Historia RAG",
    page_icon="🔍",
    layout="wide",
)

st.title("🔍 Video Historia RAG")
st.caption("Generación Aumentada por Recuperación — Streamlit + FastAPI + ChromaDB + Google AI")



with st.sidebar:
    st.header("📊 Estado del Sistema")

    health = check_api_health()

    if health is None:
        st.error("🔴 API no disponible")
        st.info("Asegúrate de que FastAPI esté corriendo:\n```\nuvicorn app.main:app --reload --port 8000\n```")
    else:
        st.success("🟢 API conectada")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ChromaDB", "✅" if health.get("chroma_accessible") else "❌")
        with col2:
            st.metric("Chunks indexados", health.get("indexed_chunks", 0))

    st.divider()

    # --- Carga de documentos ---
    st.header("📄 Cargar Documentos")
    st.caption("Sube archivos PDF, TXT o MD para indexarlos.")

    uploaded_files = st.file_uploader(
        "Selecciona archivos",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    if uploaded_files:
        st.info(f"📎 {len(uploaded_files)} archivo(s) seleccionado(s)")
        if st.button("🚀 Indexar documentos", type="primary", use_container_width=True):
            with st.spinner("Indexando... (chunkificando, embebiendo y almacenando)"):
                result = ingest_files(uploaded_files)

            if result:
                st.success(
                    f"✅ **{result['documents']}** documento(s) indexados "
                    f"con **{result['chunks']}** chunks."
                )
                st.balloons()

    st.divider()

    if st.button("Reiniciar base de datos", type="secondary", use_container_width=True):
        with st.spinner("Reiniciando base de datos..."):
            result = reset_database()

        if result:
            st.success(
                f"✅ Base de datos reiniciada."
            )



# ---------------------------------------------------------------------------
# Área principal — Preguntas y respuestas
# ---------------------------------------------------------------------------

# Verificar que la API está disponible
if health is None:
    st.warning("⚠️ Conecta la API para empezar a hacer preguntas.")
    st.stop()

# Verificar que hay documentos indexados
if health.get("indexed_chunks", 0) == 0:
    st.info("📭 No hay documentos indexados todavía. Usa el panel lateral para cargar documentos.")
    st.stop()

st.header("💬 Haz una pregunta")

# Input de pregunta
col_input, col_k = st.columns([4, 1])

with col_input:
    question = st.text_input(
        "Escribe tu pregunta:",
        placeholder="¿Qué dice el documento sobre...?",
        label_visibility="collapsed",
    )

with col_k:
    top_k = st.number_input("Top-K", min_value=1, max_value=20, value=3)

# Botón de enviar
if st.button("🔎 Preguntar", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("⚠️ Escribe una pregunta antes de enviar.")
    else:
        with st.spinner("Buscando y generando respuesta..."):
            result = query_api(question, top_k)

        if result:
            # --- Respuesta ---
            st.divider()

            if result.get("abstained"):
                st.warning("⚠️ **El sistema se abstuvo** — no hay evidencia suficiente.")

            st.subheader("📝 Respuesta")
            st.markdown(result["answer"])

            # --- Citas / Chunks ---
            st.subheader("📚 Fuentes consultadas")

            citations = result.get("citations", [])
            if citations:
                for i, cite in enumerate(citations, start=1):
                    score_pct = cite["score"] * 100
                    # Color del score
                    if score_pct >= 70:
                        score_color = "🟢"
                    elif score_pct >= 40:
                        score_color = "🟡"
                    else:
                        score_color = "🔴"

                    with st.expander(
                        f"[{i}] {cite['source']} — {score_color} Similitud: {score_pct:.1f}%"
                    ):
                        st.markdown(f"**Archivo:** `{cite['source']}`")
                        st.markdown(f"**Score:** {cite['score']:.4f}")
                        st.markdown(f"**ID:** `{cite['chunk_id']}`")
                        st.divider()
                        st.markdown(cite["text"])
            else:
                st.info("No se encontraron chunks relevantes.")
