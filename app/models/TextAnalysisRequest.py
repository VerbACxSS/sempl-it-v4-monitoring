from pydantic import BaseModel, Field


class TextAnalysisRequest(BaseModel):
    text: str = Field(max_length=5000)
