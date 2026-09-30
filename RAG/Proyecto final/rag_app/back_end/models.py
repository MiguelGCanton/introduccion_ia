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


