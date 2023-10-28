from config.database import Base
from sqlalchemy import Column, String, Integer


class CategoriaNoticia(Base):

    __tablename__  = 'categoria_noticias'

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String, unique=True)
