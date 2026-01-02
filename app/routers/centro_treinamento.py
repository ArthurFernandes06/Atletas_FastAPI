from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm  import Session

from schemas.centro_treinamento import CentroTreinamentoCreate
from models.centro_treinamento import CentroTreinamentoModel
from core.database import get_db


router = APIRouter(prefix="/centro_treinamento", tags=["Centro de treinamento"])

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_centro_treinamento(
    centro_treinamento: CentroTreinamentoCreate,
    db: Session = Depends(get_db)
):
    novo_centro_treinamento = CentroTreinamentoModel(**centro_treinamento.model_dump())

    db.add(novo_centro_treinamento)
    db.commit()
    db.refresh(novo_centro_treinamento)

    return novo_centro_treinamento

@router.get("/")
def listar_centro_treinamento(db: Session = Depends(get_db)):
    centro_treinamentos = db.query(CentroTreinamentoModel).all()
    return centro_treinamentos

@router.delete("/{centro_treinamento_id}",status_code=status.HTTP_204_NO_CONTENT)
def deletar_centro_treinamento(
    centro_treinamento_id: int,
    db: Session = Depends(get_db)
):
    centro_treinamento= db.query(CentroTreinamentoModel).filter(
        CentroTreinamentoModel.pk_id == centro_treinamento_id
    ).first()

    if not centro_treinamento:
        raise HTTPException(status_code=404, detail= "Centro de treinamento não encontrado.")
    
    db.delete(centro_treinamento)
    db.commit()