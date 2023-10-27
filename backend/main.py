from fastapi import FastAPI
from config.database import engine
from models.usuario import Base
from routes import usuario


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(usuario.router)