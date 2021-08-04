from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from src.schemas.schema import LoginSchema, LoginSuccessSchema
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider, token_provider

from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()


@router.post('/token')
def login(login: LoginSchema, session: Session = Depends(get_db)):
    email = login.email
    passwd = login.password

    user = UserRepository(session).searchEmail(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="E-mail não existe em nossa base.")

    pass_valid = hash_provider.verify_hash(passwd, user.password)
    if not pass_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="A senha está incorreta")

    # Gererate Token JWT
    token = token_provider.create_access_token({'sub': user.email})
    return LoginSuccessSchema(user=user, access_token=token)
