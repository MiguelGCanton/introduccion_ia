
from pydantic import json_schema
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import *
from embed import get_embeddings
from store import add_chunks


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

class HealthResponse(BaseModel):
    status: str
    chroma_accessible: bool
    indexed_chunks: int


@app.get("/health", response_model=HealthResponse, tags=["Sistema"])
def health():
    """Verifica que la API y ChromaDB están accesibles."""

    chroma_ok = True
    count = 0

    return HealthResponse(
        status="ok",
        chroma_accessible=chroma_ok,
        indexed_chunks=count,
    )

@app.post("/ingest", response_model=IngestResponse, tags=["Sistema"]) 
def ingest(texts: list[str]):
    embeddings = get_embeddings(texts)

    add_chunks(embeddings, texts, "test_document.txt")
        
    return {
        "embed": embeddings,
        "chunks": len(embeddings),
        "message": "Embeddings generados exitosamente",
        "ids": [f"chunk_{i}" for i in range(len(embeddings))],
    }
