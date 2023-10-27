from typing import List
from pydantic import BaseModel


class NoticiaRequest(BaseModel):

    titulo: str
    contenido: str
    fecha_publicacion: str
    imagen: List[str]
    estado: bool

    usuario_id: int
    categoria_id: int

    class Config:
        json_schema_extra = {
            'example': {
                'titulo': 'Descubre Cusco',
                'contenido': 'Lorem Ipsum is simply dummy text.',
                'fecha_publicacion': '2020-11-24',
                'imagen': ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg'],
                'estado': False,
                'usuario_id': 1,
                'categoria_id': 2
            }
        }
    