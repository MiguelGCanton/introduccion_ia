from pydantic import Field
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    chroma_accessible: bool
    indexed_chunks: int

class IngestResponse(BaseModel):
    documents: int
    chunks: int
    message: str
    ids: list[str]

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="Pregunta del usuario")
    top_k: int = Field(default=3, ge=1, le=20, description="Número de chunks a recuperar")


class Citation(BaseModel):
    chunk_id: str
    source: str
    text: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    citations: list[Citation]
    abstained: bool
