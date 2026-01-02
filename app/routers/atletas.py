from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models.atletas import AtletasModel
from schemas.atletas import AtletaCreate
from core.database import get_db

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.post("/",status_code=status.HTTP_201_CREATED)
def create_atleta(
    atleta: AtletaCreate,
    db: Session = Depends(get_db)
):
    novo_atleta = AtletasModel(**atleta.model_dump())

    db.add(novo_atleta)
    db.commit()
    db.refresh(novo_atleta)

    return novo_atleta

@router.get("/")
def listar_atletas(db: Session = Depends(get_db)):
    atletas = db.query(AtletasModel).all()
    return atletas

@router.delete("/{atletas_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_atleta(
    atleta_id: int,
    db: Session = Depends(get_db)
):
    atleta = db.query(AtletasModel).filter(
        AtletasModel.pk_id == atleta_id
    ).fisrt()

    if not atleta:
        raise HTTPException(status_code=404, detail="atleta não encontrado")
    
    db.delete(atleta)
    db.commit()