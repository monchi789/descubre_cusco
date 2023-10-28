from pydantic import BaseModel


class UsuarioRequest(BaseModel):

    usuario: str
    telefono: str
    correo: str
    nombres: str
    apellidos: str
    contrasena: str
    rol: str

    class Config: 
        json_schema_extra = {
            'example' : {
                'usuario': 'usuario1',
                'telefono': '987654321',
                'correo': 'usuario@example.com',
                'nombres': 'Paco',
                'apellidos': 'Bazan',
                'contrasena': '1234',
                'rol': 'admin'
            }
        }
