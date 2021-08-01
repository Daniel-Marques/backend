from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.config.database import get_db

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()


@router.get('/users', status_code=status.HTTP_200_OK, tags=["Users"])
def index(db: Session = Depends(get_db)):
    return UserRepository(db).index()


@router.post('/users', tags=["Users"])
def create(user: UserSchema, db: Session = Depends(get_db)):
    user_created = UserRepository(db).create(user)
    return user_created


@router.put('/users/{id}', tags=["Users"])
def update(id: int, user: UserSchema, db: Session = Depends(get_db)):
    user_updated = UserRepository(db).update(id, user)
    return user


@router.get('/users/{user_id}', tags=["Users"])
def show(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).show(user_id)
    return user


@router.delete('/users/{user_id}', tags=["Users"])
def destroy(user_id: int, db: Session = Depends(get_db)):
    UserRepository(db).destroy(user_id)
    return {'message': 'Usuário removido com sucesso.'}
