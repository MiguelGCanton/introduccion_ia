
from fastapi import File, UploadFile, HTTPException
from pydantic import json_schema
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from embed import get_embeddings
from store import add_chunks, get_collection_count,query_similar, reset_chromadb
from generate import generate_answer
from chunk import read_file_content, chunk_text

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not GOOGLE_API_KEY:
        print("⚠️  GOOGLE_API_KEY no configurada. Configúrala en .env")
    else:
        print("✅ GOOGLE_API_KEY detectada")
    yield


app = FastAPI(
    title="RAG API con Gemini",
    description="API RAG que permite subir documentos PDF para luego preguntar sobre su contenido usando Gemini.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse, tags=["Sistema"])
def health():
    """Verifica que la API y ChromaDB están accesibles."""
    try:
        count = get_collection_count()
        chroma_ok = True
    except Exception:
        count = 0
        chroma_ok = False

    return HealthResponse(
        status="ok",
        chroma_accessible=chroma_ok,
        indexed_chunks=count,
    )

@app.post("/ingest", response_model=IngestResponse, tags=["Sistema"]) 
async def ingest(files: list[UploadFile] = File(...)):

    total_ids= []
    for file in files:
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No se proporcionó un archivo con nombre válido."
            )

        content_bytes = await file.read()
        try:
            texts = read_file_content(content_bytes, file.filename)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        chunks =chunk_text(texts)
        embeddings = get_embeddings(chunks)
        
        ids = add_chunks(embeddings, chunks, file.filename)
        total_ids += ids
    return IngestResponse(
        documents= len(files),
        chunks= len(total_ids),
        message= "Embeddings generados exitosamente",
        ids= total_ids
    )

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):

    count = get_collection_count()
    if count == 0:
        raise HTTPException(
            status_code=400,
            detail="No hay documentos indexados. Usa /ingest primero.",
        )
    
    embeded_question = get_embeddings([request.question])

    results = query_similar(embeded_question[0], top_k=request.top_k)

    response = generate_answer(request.question, results)

    citations = [
        Citation(
            chunk_id=r["id"],
            source=r["source"],
            text=r["text"],
            score=r["score"],
        )
        for r in results
    ]
    return QueryResponse(
        answer=response['answer'],
        citations=citations,
        abstained=response['abstained']
    )
 
@app.get("/reset")
def reset():
    reset_chromadb()
    return {
        "operation": "sucess, db restored"
    }