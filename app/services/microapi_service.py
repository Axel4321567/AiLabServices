from typing import Any, List
from app.models.schemas import OutputItem, Metric, ChartDataItem
from app.repositories.dummy_repo import DummyRepo
from pymongo import MongoClient
from app.core.config import settings  # <--- Importa settings

class MicroApiService:
    def __init__(self, repo: DummyRepo = None):
        self.repo = repo or DummyRepo()
        # Usa settings para la configuración de MongoDB
        self.client = MongoClient(settings.mongo_uri)
        self.db = self.client[settings.mongo_db]
        self.metrics_collection = self.db["metrics"]

    def get_all_metrics(self) -> str:
        return "Ok"
    
    def get_metrics(self) -> List[Metric]:
        metrics = []
        for doc in self.metrics_collection.find():
            # Elimina _id de Mongo para evitar conflictos con Pydantic
            doc.pop('_id', None)
            chart_data = [ChartDataItem(**item) for item in doc.get("chartData", [])]
            metric = Metric(
                name=doc["name"],
                value=doc["value"],
                chartData=chart_data
            )
            metrics.append(metric)
        return metrics

    def procesar(self, container: Any) -> List[OutputItem]:
        if isinstance(container, dict):
            items = list(container.values())
        elif isinstance(container, list):
            items = container
        else:
            raise ValueError("Formato no soportado: se esperaba dict o list")
        
        procesados: List[OutputItem] = []
        for item in items:
            raw_id = item.get("id")
            raw_val = item.get("valor")
            if raw_id is None or raw_val is None:
                raise ValueError("Cada elemento debe tener 'id' y 'valor'")
            
            nuevo_valor = self._calcula(raw_val)
            procesados.append(OutputItem(id=str(raw_id), valor=nuevo_valor))
        
        self.repo.save_all(procesados)
        return procesados

    def _calcula(self, x: Any) -> float:
        return float(x) * 2
