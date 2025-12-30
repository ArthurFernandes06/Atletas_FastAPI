from core.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship


class CategoriasModel(Base):
    __tablename__ = "categorias"

    pk_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(32), nullable=False)
    nome = Column(String(31),nullable=False)

    atletas = relationship(
        "AtletasModel",
        back_populates="categoria",
        cascade="all, delete-orphan",
        passive_deletes=True
    )