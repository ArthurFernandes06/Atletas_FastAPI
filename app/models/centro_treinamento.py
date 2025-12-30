from core.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship


class CentroTreinamentoModel(Base):
    __tablename__ = "centro_treinamento"

    pk_id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String(50),unique=True, nullable=False)
    endereco = Column(String(60),nullable=False)
    proprietario = Column(String(50), nullable=False)

    atletas = relationship(
        "AtletasModel",
        back_populates="centro_treinamento",
        cascade="all, delete-orphan",
        passive_deletes=True
    )