from pydantic import BaseModel


class CentroTreinamentoCreate(BaseModel):
    nome: str
    endereco: str
    proprietario: str