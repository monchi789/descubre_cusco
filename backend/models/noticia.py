from config.database import Base
from sqlalchemy import Integer, ForeignKey, String, Column, Date, Boolean, ARRAY


class Noticia(Base):

    __tablename__ = 'noticias'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    contenido = Column(String)
    fecha_publicacion = Column(Date)
    imagen = Column(ARRAY(String))
    estado = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    categoria_noticia_id = Column(Integer, ForeignKey('categoria_noticias.id'))
