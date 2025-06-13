from pydantic import BaseModel
from typing import Any

class InputContainer(BaseModel):
    data: Any

class OutputItem(BaseModel):
    id: str
    valor: float