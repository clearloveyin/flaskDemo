from pydantic import BaseModel, Field
from typing import Optional


class DemoSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID")
    name: str = Field(description="名称")