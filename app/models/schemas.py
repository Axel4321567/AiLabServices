from pydantic import BaseModel
from typing import List

class OutputItem(BaseModel):
    id: str
    valor: float


class ChartDataItem(BaseModel):
    name: str
    value: int

class Metric(BaseModel):
    name: str
    value: int
    chartData: List[ChartDataItem]
