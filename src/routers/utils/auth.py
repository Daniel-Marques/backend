from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_user_loggedin(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not phone:
        raise exception

    user = UserRepository(session).get_by_phone(phone)

    if not user:
        raise exception

    return user
