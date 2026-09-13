from pydantic import BaseModel, Field


class MonitoringResponse(BaseModel):
    monitoring_id: int = Field(serialization_alias="monitoringId")
