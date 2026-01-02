from fastapi import FastAPI
from routers.atletas import router as atletas_router
from routers.categorias import router as categorias_router
from routers.centro_treinamento import router as centro_treinamento


app = FastAPI()

app.include_router(atletas_router)
app.include_router(categorias_router)
app.include_router(centro_treinamento)

@app.get("/")
async def root():
    return {"message": "API FUNCIONANDO"}