from fastapi import APIRouter, HTTPException, status, Path
from config.database import db_dependency
from models.usuario import Usuario
from schemas.usuario import UsuarioRequest

router = APIRouter(
    tags=['Usuarios']
)


@router.get('/usuarios/', status_code=status.HTTP_200_OK)
async def get_all_usuarios(db: db_dependency):

    return db.query(Usuario).all()


@router.get('/usuarios/', status_code=status.HTTP_200_OK)
async def get_usuario_by_id(db: db_dependency, usuario_id: int = Path(gt=0)):

    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
async def create_usuario(db: db_dependency, usuario_request: UsuarioRequest):

    usuario_model = Usuario(**UsuarioRequest.model_dump())
    db.add(usuario_model)
    db.commit()


@router.put('/usuarios', status_code=status.HTTP_204_NO_CONTENT)
async def update_usuarios(db: db_dependency, usuario_request: UsuarioRequest, usuario_id: int = Path(gt=0)):
    
    usuario_model = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if usuario_model is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    
    usuario_model.usuario = usuario_request.usuario
    usuario_model.telefono = usuario_request.telefono
    usuario_model.correo = usuario_request.correo
    usuario_model.nombres = usuario_request.nombres
    usuario_model.apellidos = usuario_request.apellidos
    usuario_model.contrasena = usuario_request.contrasena
    usuario_model.rol = usuario_request.rol

    db.add(usuario_model)
    db.commit()


@router.delete('/usuarios', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(db: db_dependency, usuario_id: int = Path(gt=0)):

    usuario_model = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if usuario_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    
    db.query(Usuario).filter(Usuario.id == usuario_id).delete()

    db.commit()
    