from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    chroma_accessible: bool
    indexed_chunks: int
