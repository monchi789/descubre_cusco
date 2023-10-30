from fastapi import APIRouter, status, HTTPException, Path
from  config.database import db_dependency
from schemas.categoria_noticia import CategoriaNoticiaRequest
from models.categoria_noticia import CategoriaNoticia


router = APIRouter(
    tags=['Categoria de Noticias']
)


@router.get('/categoria_noticias/', status_code=status.HTTP_200_OK)
async def get_all_categoria_noticias(db: db_dependency):

    return db.query(CategoriaNoticia).all()


@router.get('/categoria_noticia/', status_code=status.HTTP_200_OK)
async def get_categoria_noticia_by_id(db: db_dependency, categoria_noticia_id: int = Path(gt=0)):

    return db.query(CategoriaNoticia).filter(CategoriaNoticia.id == categoria_noticia_id).first()


@router.post('/categoria_noticia', status_code=status.HTTP_201_CREATED)
async def create_categoria_noticia(db: db_dependency, categoria_noticia_request: CategoriaNoticiaRequest):

    categoria_noticia_model = CategoriaNoticia(**categoria_noticia_request.model_dump())

    db.add(categoria_noticia_model)
    db.commit()


@router.put('/categoria_noticia/{categoria_noticia_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_categoria_noticia(db: db_dependency, categoria_noticia_request: CategoriaNoticiaRequest, categoria_noticia_id: int = Path(gt=0)):

    categoria_noticia_model = db.query(CategoriaNoticia).filter(CategoriaNoticia.id == categoria_noticia_id).first()

    if categoria_noticia_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Categoria de Noticia no encontrada')
    
    categoria_noticia_model.id = categoria_noticia_request.id
    categoria_noticia_model.categoria = categoria_noticia_request.categoria

    db.add(categoria_noticia_model)
    db.commit()


@router.delete('/categoria_noticia/{categoria_noticia_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria_noticia(db: db_dependency, categoria_noticia_id: int = Path(gt=0)):

    categoria_noticia_model = db.query(CategoriaNoticia).filter(CategoriaNoticia.id == categoria_noticia_id).first()

    if categoria_noticia_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Categoria de Noticia no encontrada')


    db.query(CategoriaNoticia).filter(CategoriaNoticia.id == categoria_noticia_id).delete()
    db.commit()
    