from typing import List
from app.models.schemas import OutputItem

class DummyRepo:
    def save_all(self, items: List[OutputItem]) -> None:
        # Aquí podrías implementar la lógica de persistencia o envío a colas
        print(f"Guardando {len(items)} items en repositorio.")