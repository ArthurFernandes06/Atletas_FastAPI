from core.database import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship

#Aqui temos o model de Atletas, serve de base para guardar as respectivas
#informações na tabela atletas.
class AtletasModel(Base):
    __tablename__ = "atletas"

    pk_id = Column(Integer, primary_key=True, autoincrement=True)#id relacional
    id = Column(String(50), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(16),unique=True,nullable=False)
    idade = Column(Integer,nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1))
    #Chaves estrangeiras, das tabelas centro_treinamento e categoria.
    centro_treinamento_id = Column(Integer, ForeignKey('centro_treinamento.pk_id', ondelete="CASCADE"), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.pk_id', ondelete="CASCADE"), nullable=False)

    centro_treinamento = relationship(
        "CentroTreinamentoModel",
        back_populates="atletas"
    )

    categoria = relationship(
        "CategoriasModel",
        back_populates="atletas"
    )