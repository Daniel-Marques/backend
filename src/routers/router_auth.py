from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.config.database import get_db

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/token')
def login(login):
    pass
