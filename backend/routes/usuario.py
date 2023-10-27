from fastapi import APIRouter, HTTPException, status, Path
from config.database import db_dependency
from models.usuario import Usuario

router = APIRouter(
    tags=['Usuarios']
)


@router.get('/usuarios/', status_code=status.HTTP_200_OK)
async def get_all_usuarios(db: db_dependency):

    return db.query(Usuario).all()


@router.get('/usuarios/', status_code=status.HTTP_200_OK)
async def get_all_usuarios_by_id(db: db_dependency, usuario_id: int = Path(gt=0)):

    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


# @router.post('/usuarios', status_code=status.HTTP_201_CREATED)
# async def create