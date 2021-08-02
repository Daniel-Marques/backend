from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.config.database import get_db

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()

@router.get('/')
async def welcome():
    return 'API Rest em Python para desafio PontoTel'

@router.get('/users', status_code=status.HTTP_200_OK, tags=["Users"])
async def index(db: Session = Depends(get_db)):
    return UserRepository(db).index()


@router.post('/users', tags=["Users"])
async def create(user: UserSchema, db: Session = Depends(get_db)):
    user_created = UserRepository(db).create(user)
    return user_created


@router.put('/users/{id}', tags=["Users"])
async def update(id: int, user: UserSchema, db: Session = Depends(get_db)):
    user_updated = UserRepository(db).update(id, user)
    return user


@router.get('/users/{user_id}', tags=["Users"])
async def show(user_id: int, db: Session = Depends(get_db)):
    try:
        user_found = UserRepository(db).show(user_id)
        return user_found
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.delete('/users/{user_id}', tags=["Users"])
async def destroy(user_id: int, db: Session = Depends(get_db)):
    UserRepository(db).destroy(user_id)
    return {'message': 'Usuário removido com sucesso.'}
