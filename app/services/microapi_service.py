from typing import Any, List
from app.models.schemas import OutputItem
from app.repositories.dummy_repo import DummyRepo

class MicroApiService:
    def __init__(self, repo: DummyRepo = None):
        self.repo = repo or DummyRepo()

    def procesar(self, container: Any) -> List[OutputItem]:
        # Normalizar a lista de dicts
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
        
        # Persistir o enviar a otro servicio
        self.repo.save_all(procesados)
        return procesados

    def _calcula(self, x: Any) -> float:
        return float(x) * 2