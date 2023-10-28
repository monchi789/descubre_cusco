from pydantic import BaseModel


class CategoriaNoticiaRequest(BaseModel):

    nombre: str 

    class Config: 
        json_schema_extra = {
            'example': {
                'nombre': 'turismo'
            }
        }
        