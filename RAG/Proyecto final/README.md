# Sistema RAG — Asistente de Consulta Documental
### Proyecto Final: Introducción a la Inteligencia Artificial
**Stack:** Streamlit + FastAPI + ChromaDB + Google AI Studio (Gemini)

---

## ⚡ Inicio Rápido (Cómo Ejecutar el Proyecto)

Para correr el sistema completo se requieren **dos terminales** abiertas en la raíz del proyecto (`Proyecto final`) con el entorno virtual activado:

```bash
# Terminal 1: Iniciar API Backend (FastAPI)
uvicorn main:app --reload --app-dir "rag_app/back_end" --port 8000

# Terminal 2: Iniciar Interfaz de Usuario (Streamlit)
streamlit run rag_app/ui/streamlint_app.py
```

- **Frontend (Streamlit):** [http://localhost:8501](http://localhost:8501)
- **API Docs (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📖 Descripción del Proyecto

Este proyecto implementa un sistema completo de **Generación Aumentada por Recuperación (RAG)** siguiendo una arquitectura desacoplada en tres capas:

1. **Interfaz de Usuario (UI):** Desarrollada en **Streamlit** para permitir la carga de documentos, consulta conversacional, visualización de respuestas fundamentadas y despliegue interactivo de citas con métricas de similitud.
2. **API Backend:** Desarrollada con **FastAPI**, expone los servicios para ingesta documental, vectorización, persistencia, consulta semántica y orquestación con modelos generativos.
3. **Persistencia e Indexación:** Base de datos vectorial persistente en disco con **ChromaDB**, usando distancia coseno.
4. **Embeddings y Generación:** Modelos de **Google AI Studio** a través del SDK `google-genai`:
   - **Embeddings:** `gemini-embedding-001` (tanto para documentos como para preguntas).
   - **Generación:** `gemini-3.8-flash` con instrucciones estrictas de anclaje a evidencia, citas numeradas `[n]` y abstención automática si no hay contexto suficiente.

---

## 🏛️ Arquitectura del Sistema

```
Usuario
  │
  ▼
Streamlit (Puerto 8501)
  │  (HTTP / JSON)
  ▼
FastAPI (Puerto 8000)
  ├── 1. Google AI Studio   ───► Generación de embeddings (gemini-embedding-001)
  ├── 2. ChromaDB           ───► Persistencia vectorial local y búsqueda k-NN
  └── 3. Google AI Studio   ───► Síntesis anclada y citas (gemini-3.8-flash)
```

---

## 📁 Estructura del Repositorio

```text
Proyecto final/
├── README.md                      # Instrucciones de instalación y uso
├── requirements.txt               # Dependencias del proyecto
├── .env.example                   # Plantilla de variables de entorno
├── .env                           # Llaves de API (excluido en .gitignore)
├── chroma/                        # Almacenamiento local persistente de ChromaDB
├── rag_app/
│   ├── back_end/
│   │   ├── main.py                # Endpoints FastAPI (/health, /ingest, /query, /reset)
│   │   ├── models.py              # Esquemas Pydantic para request/response
│   │   ├── chunk.py               # Lógica de extracción de texto y chunking con overlap
│   │   ├── embed.py               # Cliente de embeddings con Google AI
│   │   ├── store.py               # Operaciones con ChromaDB (ingesta y búsqueda k-NN)
│   │   ├── generate.py            # Prompt engineering y generación con Gemini
│   │   └── data/                  # Carpeta para documentos del corpus
│   └── ui/
│       └── streamlint_app.py      # Interfaz de usuario interactiva en Streamlit
```

---

## 🚀 Requisitos Previos e Instalación

### 1. Requisitos
- **Python 3.10 o superior**
- Clave de API de Google AI Studio gratuita. Puedes obtenerla en:
  👉 [Google AI Studio — Get API Key](https://aistudio.google.com/apikey)

---

### 2. Clonar el repositorio y crear el entorno virtual

Abre tu terminal y ubícate en la carpeta raíz del proyecto:

```bash
cd "RAG/Proyecto final"
```

Crea y activa un entorno virtual de Python:

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **En Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

---

### 3. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Configurar la clave de API (`.env`)

Crea un archivo `.env` en la raíz del proyecto a partir de `.env.example`:

```bash
cp .env.example .env
```

Edita el archivo `.env` y agrega tu clave de API:

```env
GOOGLE_API_KEY="AIzaSy..."
```

> ⚠️ **Seguridad:** El archivo `.env` contiene credenciales secretas y está incluido en `.gitignore` para no ser subido al control de versiones.

---

## ▶️ Ejecución del Proyecto

Para correr la aplicación se necesitan **dos terminales** simultáneas con el entorno virtual activado:

### Terminal 1: Iniciar la API Backend (FastAPI)

Desde la carpeta raíz del proyecto (`Proyecto final`), ejecuta:

```bash
uvicorn main:app --reload --app-dir "rag_app/back_end" --port 8000
```

- La API estará disponible en: [http://localhost:8000](http://localhost:8000)
- Documentación interactiva Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Terminal 2: Iniciar la Interfaz Web (Streamlit)

Abre una **segunda terminal**, asegúrate de activar el entorno virtual y ejecuta:

```bash
streamlit run rag_app/ui/streamlint_app.py
```

- La aplicación abrirá automáticamente en tu navegador en: [http://localhost:8501](http://localhost:8501)

---

## 💡 Guía de Uso del Sistema

1. **Monitoreo del Estado:**
   - En el panel lateral de Streamlit se muestra el estado en tiempo real de la conexión con FastAPI y ChromaDB, además del contador de fragmentos indexados.

2. **Ingesta de Documentos:**
   - En el panel lateral, usa la opción **"Cargar Documentos"**.
   - Selecciona archivos en formato `.pdf`, `.txt` o `.md` (por ejemplo, los archivos de la carpeta `rag_app/back_end/data/`).
   - Presiona **"🚀 Indexar documentos"**.
   - El sistema dividirá los textos en chunks de 300 palabras con 60 palabras de solape, generará los vectores mediante `gemini-embedding-001` y los persistirá en `chroma/`.

3. **Consulta de Información:**
   - Escribe tu pregunta en el campo de texto central.
   - Ajusta el parámetro **Top-K** (cantidad de fragmentos más similares a recuperar, por defecto `3`).
   - Haz clic en **"🔎 Preguntar"**.

4. **Respuesta y Citas:**
   - La respuesta generada por Gemini citará las fuentes con formato `[1]`, `[2]`, etc.
   - En la sección **"📚 Fuentes consultadas"** podrás desplegar cada fragmento utilizado, viendo:
     - Nombre del archivo de origen.
     - Identificador único del chunk.
     - Score y porcentaje de similitud semántica con semáforo de relevancia (🟢 $\ge 70\%$, 🟡 $\ge 40\%$, 🔴 $< 40\%$).
     - Texto exacto del fragmento recuperado.

---

## 🧪 Pruebas Sugeridas (Validación de Evidencia y Abstención)

El corpus de prueba está enfocado en **Historia, Diseño, Hardware e Impacto Cultural de los Videojuegos**:

### Preguntas dentro de dominio (Deben responder con citas reales)
1. **Crisis de la industria y recuperación:**
   > *"¿Cuáles fueron las causas de la crisis de los videojuegos de 1983 y cómo logró Nintendo revitalizar el mercado?"*
2. **Evolución del hardware:**
   > *"¿Qué avances técnicos introdujeron las consolas de quinta generación respecto a las de generaciones anteriores?"*
3. **Diseño de juegos:**
   > *"¿Cuáles son los principios fundamentales del diseño de niveles y la curva de dificultad en videojuegos?"*

### Pregunta fuera de dominio (Prueba de abstención)
4. **Pregunta imposible de responder con el corpus:**
   > *"¿Cuál es la receta tradicional para preparar pasta a la carbonara con guanciale?"*
   - **Comportamiento esperado:** El sistema activa el protocolo de abstención, informando que no cuenta con evidencia suficiente en los documentos y no genera alucinaciones ni utiliza conocimiento paramétrico ajeno al corpus.

---

## 🛡️ Criterios de Chunking y Abstención

- **Estrategia de Chunking:**
  - `chunk_size = 300` palabras.
  - `overlap = 60` palabras (20% de solape).
  - Justificación: Permite mantener la cohesión de ideas y evita que conceptos clave queden divididos abruptamente en los límites del fragmento.
- **Criterio de Abstención:**
  - **Filtro de Similitud Semántica:** Se establece un umbral mínimo `MIN_SCORE = 0.30` en distancia de coseno convertida a similitud ($1 - \text{distancia}$). Si ningún fragmento alcanza el umbral, se aborta la generación y se retorna abstención directamente.
  - **Prompt de Anclaje Estricto:** Se instruye al modelo Gemini a responder únicamente con la evidencia numerada y a emitir explícitamente el mensaje de abstención si la información no responde con certeza la pregunta.

---

## 📡 Endpoints de la API (FastAPI)

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/health` | Chequeo de salud del servicio y disponibilidad de ChromaDB con conteo de chunks. |
| `POST` | `/ingest` | Recibe archivos multipart (`.pdf`, `.txt`, `.md`), los fragmenta, vectoriza y persiste. |
| `POST` | `/query` | Recibe `question` y `top_k`, busca vecinos más cercanos en Chroma y sintetiza la respuesta con Gemini. |
| `GET` | `/reset` | Restaura y limpia la colección de ChromaDB para pruebas limpias. |
| `GET` | `/docs` | Interfaz Swagger interactiva para pruebas de endpoints. |
