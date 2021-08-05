from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.models.user_model import UserModel
from src.routers.utils.auth import get_user_loggedin
from src.schemas.schema import UserSchema, UserWithoutPasswordSchema
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()


@router.get('/')
async def welcome():
    return {'message': {
        'description': 'API Rest em Python para desafio PontoTel',
        'author': {
            'name': 'Daniel Marques',
            'email': 'daniel.silva.city@gmail.com'
        }
    }}


@router.get('/users', tags=["Users"])
async def index(db: Session = Depends(get_db), user: UserModel = Depends(get_user_loggedin)):
    user_list = UserRepository(db).index()
    return user_list


@router.post('/users', tags=["Users"])
async def create(user: UserSchema, db: Session = Depends(get_db), userAuth: UserModel = Depends(get_user_loggedin)):
    # Verify has user by phone

    # Create new user
    user.password = hash_provider.create_hash(user.password)
    user_created = UserRepository(db).create(user)
    return user_created


@router.put('/users/{id}', tags=["Users"])
async def update(id: int, user: UserSchema, db: Session = Depends(get_db), userAuth: UserModel = Depends(get_user_loggedin)):
    user_search = UserRepository(db).getUser(id)

    if(user.password is None):
        user.password = user_search.password
    else:
        user.password = hash_provider.create_hash(user.password)
    print(user)
    return UserRepository(db).update(id, user)


@router.get('/users/{user_id}', tags=["Users"])
async def show(user_id: int, db: Session = Depends(get_db), user: UserModel = Depends(get_user_loggedin)):
    try:
        user_found = UserRepository(db).show(user_id)
        return user_found
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.get('/users/document/{document}', tags=["Users"])
async def searchDocument(document: str, db: Session = Depends(get_db), user: UserModel = Depends(get_user_loggedin)):
    user_found = UserRepository(db).searchDocument(document)
    return user_found


@router.get('/users/email/{email}', tags=["Users"])
async def searchEmail(email: str, db: Session = Depends(get_db)):
    user_found = UserRepository(db).searchEmail(email)
    return user_found


@router.delete('/users/{user_id}', tags=["Users"])
async def destroy(user_id: int, db: Session = Depends(get_db), user: UserModel = Depends(get_user_loggedin)):
    UserRepository(db).destroy(user_id)
    return {'message': 'Usuário removido com sucesso.'}
