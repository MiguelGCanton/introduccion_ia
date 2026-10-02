# Reporte Técnico: Sistema RAG (Proyecto Final)

**Asignatura:** Introducción a la Inteligencia Artificial  
**Autor:** Miguel G. Cantón  
**Stack Tecnológico:** Streamlit (UI) + FastAPI (API) + ChromaDB (Vector Store) + Google AI Studio (Gemini)  

---

## 1. Dominio y tamaño del corpus

Para este proyecto utilicé gemini 3.8 flash para generar toda la informacion necesaria para el desarrollo del mismo. Me enfoque en lo siguiente:

- **Dominio temático:** El corpus aborda la **historia, evolución tecnológica, teoría del diseño, géneros e impacto sociocultural de la industria de los videojuegos**. 
- **Composición de documentos:** Se construyó a partir de **6 documentos modulares** en formato Markdown (`.md`) ubicados en `rag_app/back_end/data/`:
  1. `01_historia_videojuegos.md`: Orígenes, Spacewar!, crisis del videojuego de 1983 y rescate comercial por Nintendo.
  2. `02_generos_videojuegos.md`: Taxonomía y mecánicas esenciales (RPG, FPS, estrategia, plataformas, simulación).
  3. `03_consolas_videojuegos.md`: Cronología de nueve generaciones de hardware (desde Magnavox Odyssey hasta PS5 / Xbox Series).
  4. `04_impacto_cultural.md`: Fenómeno de los esports, comunidades online, narrativa y debates sobre accesibilidad y violencia.
  5. `05_diseno_videojuegos.md`: Gameplay loops, curva de dificultad (teoría del flujo), level design y balance de economías.
  6. `06_videojuegos_en_la_actualidad.md`: Motores gráficos (Unreal Engine 5), juego en la nube, VR/AR y modelos de monetización.
- **Modelo de Embeddings:** Se utiliza **`gemini-embedding-001`** de Google AI Studio a través del SDK oficial `google-genai`. Genera vectores para los fragmentos del corpus y las preguntas de los usuarios.

---

## 2. Estrategia de partición (Chunking) y justificación

- **Configuración:** Tamaño de fragmento (`chunk_size`) de **300 palabras** con un solape (`overlap`) de **60 palabras** (20% de solape).
- **Justificación técnica:**

  Experimentando un poco, me di cuenta que menos de 100 era muy poco para contestar preguntas variadas y para conseguir una respuesta adecuada, ademas al tener que aplicar un translape de al menos un 20% los chunks quedaban demasiado pequeños entonces si encuentra la pregunta, pero no contiene informacion suficiente para realmente resolver la duda.

  En el caso de hacerlo aun mas grande como de 600, se vuelve dificil encontrar la respuesta entre el exceso de texto que da la herramienta, por lo que considero que 300 palabras es un buen punto medio.

  El solape del 20% funciona muy bien por que es lo suficiente extenso para no cortar una respuesta a la mitad.

  Para las citaciones no hay una razon tecnica detras del numero elegido, pero considero que con un 'top_k' de 3 a 5 es suficiente para tener una respuesta satisfactoria.

---

## 3. Criterio y decisión de abstención

El sistema implementa un **protocolo de abstención en dos niveles** para evitar alucinaciones y prevenir que el modelo responda con conocimiento paramétrico ajeno al corpus:

1. **Filtro cuantitativo de similitud métrica (Pre-generación):**
   - ChromaDB calcula la distancia coseno ($d$). La API la transforma a score de similitud: $\text{score} = 1.0 - d$.
   - Se definió un umbral mínimo: **`MIN_SCORE = 0.30`**.
   - Si ningún fragmento recuperado alcanza $0.30$, el sistema **aborta la llamada a Gemini**, devuelve inmediatamente el mensaje oficial de abstención (*«No tengo evidencia suficiente en los documentos proporcionados para responder esta pregunta.»*) y marca `abstained: true`.
2. **Anclaje estricto en el prompt y detección de incertidumbre (Post-generación):**
   - Cuando hay fragmentos con score $\ge 0.30$, se le envían a Gemini numerados `[1]`, `[2]`, etc. El prompt del sistema le prohíbe explícitamente suponer o inventar datos fuera del contexto y le instruye a abstenerse si la evidencia no cubre la pregunta.
   - La API analiza el texto generado buscando frases de abstención (*«no tengo evidencia suficiente»*, *«no se encuentra en los fragmentos»*, etc.) para asegurar que el booleano `abstained` sea coherente con la respuesta visualizada en Streamlit.

---

## 4. Qué sale de Google AI vs. Qué hace ChromaDB

| Tarea | Responsable | Mecanismo |
|---|:---:|---|
| **Vectorización de textos y preguntas** | **Google AI** | Emplea `gemini-embedding-001` para mapear el significado semántico a vectores de punto flotante de 768 dimensiones. |
| **Generación de respuestas y citas** | **Google AI** | Emplea `gemini-3.8-flash` para sintetizar la respuesta final en español, anclada en los chunks provistos y citando con corchetes `[n]`. |
| **Persistencia vectorial en disco** | **ChromaDB** | Guarda localmente en la carpeta `chroma/` los identificadores, embeddings precalculados, texto de los chunks y metadatos (`source`, `chunk_index`). Reiniciar FastAPI no destruye el índice. |
| **Búsqueda geométrica ($k$-NN)** | **ChromaDB** | Ejecuta la búsqueda de vecinos más cercanos usando el índice HNSW y distancia coseno, devolviendo los `top_k` chunks más similares sin depender de embedders locales ni modelos de terceros. |
