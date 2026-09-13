from pydantic import BaseModel, Field


class ComparisonAnalysisRequest(BaseModel):
    text1: str = Field(max_length=5000)
    text2: str = Field(max_length=5000)
