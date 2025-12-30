from pydantic import BaseModel
from typing import Optional


class AtletaCreate(BaseModel):
    id: str
    nome: str
    cpf: str
    peso: float
    altura: float
    sexo: Optional[str]
    centro_treinamento_id: int
    categoria_id: int