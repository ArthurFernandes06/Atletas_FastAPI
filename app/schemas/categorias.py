from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    id: str
    nome: str