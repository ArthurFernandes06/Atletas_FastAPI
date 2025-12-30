from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine,Base
from models.atletas import AtletasModel
from models.categoria import CategoriasModel
from models.centro_treinamento import CentroTreinamentoModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Cria e atualiza as tabelas ao inicializar o servidor
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}