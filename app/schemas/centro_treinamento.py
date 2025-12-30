from pydantic import BaseModel


class CreateCentroTreinamento(BaseModel):
    nome: str
    endereco: str
    proprietario: str