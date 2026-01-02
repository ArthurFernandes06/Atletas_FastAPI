from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from models.categoria import CategoriasModel
from schemas.categorias import CategoriaCreate
from core.database import get_db

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_categoria(
    categoria: CategoriaCreate,
    db: Session = Depends(get_db)
):
    nova_categoria = CategoriasModel(** categoria.model_dump())

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria


@router.get
def listar_categorias(db: Session = Depends(get_db)):
    categorias = db.query(CategoriasModel).all()
    return categorias

@router.delete("/{categoria_id}",status_code=status.HTTP_204_NO_CONTENT)
def deletar_categoria(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    categoria = db.query(CategoriasModel).filter(
        CategoriasModel.pk_id == categoria_id
    ).first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="categoria não encontrada"
        )

    db.delete(categoria)
    db.commit()