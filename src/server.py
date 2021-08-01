from fastapi import FastAPI, Depends, status
from sqlalchemy.orm.session import Session
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.config.database import create_db, get_db

from fastapi.middleware.cors import CORSMiddleware

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

# Cria a base de dados
# create_db()

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http:127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/users', status_code=status.HTTP_200_OK)
def index(db: Session = Depends(get_db)):
    return UserRepository(db).index()

@app.post('/users')
def create(user: UserSchema, db: Session = Depends(get_db)):
    user_created = UserRepository(db).create(user)
    return user_created

@app.put('/users/{id}')
def update(id: int, user: UserSchema, db: Session = Depends(get_db)):
    user_updated = UserRepository(db).update(id, user)
    return user

@app.get('/users/{user_id}')
def show(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).show(user_id)
    return user

@app.delete('/users/{user_id}')
def destroy(user_id: int, db: Session = Depends(get_db)):
    UserRepository(db).destroy(user_id)
    return {'message': 'Usuário removido com sucesso.'}
