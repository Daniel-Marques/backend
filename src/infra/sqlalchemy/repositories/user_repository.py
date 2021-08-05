from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from src.schemas.schema import UserSchema
from src.infra.sqlalchemy.models.user_model import UserModel


class UserRepository():
    def __init__(self, db: Session):
        self.db = db

    def index(self):
        stmt = select(
            UserModel.id,
            UserModel.email,
            UserModel.pis,
            UserModel.zipcode,
            UserModel.number,
            UserModel.city,
            UserModel.country,
            UserModel.updated_at,
            UserModel.name,
            UserModel.document,
            UserModel.address,
            UserModel.complement,
            UserModel.state,
            UserModel.created_at)
        users = self.db.execute(stmt).all()
        return users

    def create(self, user: UserSchema):
        db_user = UserModel(
            name=user.name,
            document=user.document,
            pis=user.pis,
            email=user.email,
            password=user.password,
            zipcode=user.zipcode,
            address=user.address,
            number=user.number,
            complement=user.complement,
            city=user.city,
            state=user.state,
            country=user.country,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        # Alternative to hide pass
        stmt = select(
            UserModel.id,
            UserModel.email,
            UserModel.pis,
            UserModel.zipcode,
            UserModel.number,
            UserModel.city,
            UserModel.country,
            UserModel.updated_at,
            UserModel.name,
            UserModel.document,
            UserModel.address,
            UserModel.complement,
            UserModel.state,
            UserModel.created_at).where(UserModel.id == db_user.id)
        user = self.db.execute(stmt).first()
        return user

    def update(self, id: int, user: UserSchema):
        stmt = update(UserModel).where(UserModel.id == id).values(
            name=user.name,
            document=user.document,
            pis=user.pis,
            email=user.email,
            password=user.password,
            zipcode=user.zipcode,
            address=user.address,
            number=user.number,
            complement=user.complement,
            city=user.city,
            state=user.state,
            country=user.country,
        )
        self.db.execute(stmt)
        self.db.commit()
        return user

    def show(self, user_id: int):
        stmt = select(
            UserModel.id,
            UserModel.email,
            UserModel.pis,
            UserModel.zipcode,
            UserModel.number,
            UserModel.city,
            UserModel.country,
            UserModel.updated_at,
            UserModel.name,
            UserModel.document,
            UserModel.address,
            UserModel.complement,
            UserModel.state,
            UserModel.created_at).where(UserModel.id == user_id)
        user = self.db.execute(stmt).first()
        return user

    def getUser(self, id: str):
        stmt = select(UserModel).where(UserModel.id == id)
        user = self.db.execute(stmt).scalars().first()
        return user

    def searchDocument(self, document: str):
        stmt = select(UserModel).where(UserModel.document == document)
        user = self.db.execute(stmt).scalars().first()
        if(user):
            return True
        else:
            return False

    def searchEmail(self, email: str) -> UserModel:
        stmt = select(UserModel).where(UserModel.email == email)
        user = self.db.execute(stmt).scalars().first()
        return user

    def destroy(self, user_id: int):
        stmt = delete(UserModel).where(UserModel.id == user_id)
        self.db.execute(stmt)
        self.db.commit()
        return {'message': 'Usuário deletado com sucesso.'}
