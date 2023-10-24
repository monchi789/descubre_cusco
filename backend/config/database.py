import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from typing import Annotated
from fastapi import Depends


# Cargamos las variables de .env
load_dotenv()

# Acceder a las variables de entorno
SQL_ALCHEMY_DATABASE_URL = os.getenv('URL')

# Crear el motor de la base de datos
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

# Crear una sesion local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base de datos para definir los modelos
Base = declarative_base()


def get_db():

    """
        Funcion para obtener una instancia de la base de datos.

        Returns:
            Session: Una sesion de base de datos.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Anotacion para definir una dependencia de base de datos
db_dependency = Annotated[Session, Depends(get_db)]
