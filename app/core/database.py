from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Aqui estamos definindo o banco sqlite que vamos usar.
DATABASE_URL = "sqlite:///./app.db"


#Estamos conectando ao banco de dados, se ele não tiver sido criado, ele cria.
#O parametro echo=True é para aprendizado e visualizar as alterações realizadas,
#em projetos reais ele é False
engine = create_engine(DATABASE_URL, echo=True)

#Estabelece uma conexão segura com o banco de dados para executar os comandos SQL.
SessionLocal = sessionmaker(bind=engine)

#É a base que nossos models vão herdar para a orm mapear.
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()