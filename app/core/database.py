from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

#Aqui estamos definindo o banco sqlite que vamos usar.
DATABASE_URL = "sqlite:///./app.db"


#Estamos conectando ao banco de dados, se ele não tiver sido criado, ele cria.
#O parametro echo=True é para aprendizado e visualizar as alterações realizadas,
#em projetos reais ele é False
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


#Ativa as chaves estrangeiras no sqlite
@event.listens_for(engine, "connect")
def enable_sqlite_fk(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
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