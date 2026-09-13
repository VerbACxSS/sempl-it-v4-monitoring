from pydantic import BaseModel, Field

class SimplificationRequest(BaseModel):
    mode: str = Field(default='', serialization_alias="mode")
    original: str = Field(default='', serialization_alias="original")
    proofreading: str = Field(default='', serialization_alias="proofreading")
    lex: str = Field(default='', serialization_alias="lex")
    connectives: str = Field(default='', serialization_alias="connectives")
    expressions: str = Field(default='', serialization_alias="expressions")
    sentence_splitter: str = Field(default='', serialization_alias="sentence_splitter")
    nominalizations: str = Field(default='', serialization_alias="nominalizations")
    verbs: str = Field(default='', serialization_alias="verbs")
    sentence_reorganizer: str = Field(default='', serialization_alias="sentence_reorganizer")
    explain: str = Field(default='', serialization_alias="explain")

    def __getitem__(self, item):
        return getattr(self, item)

    def update(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)