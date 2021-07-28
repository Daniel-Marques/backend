from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class UserRepository():
    def __init__(self, db: Session):
        self.db = db


def index(self):
    users = self.db.query(models.User).all()
    return users


def create(self, user: schemas.User):
    db_user = models.User(
        name=user.name,
        email=user.email,
        document=user.document,
        pis=user.pis,
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
    return db_user

def show():
    pass

def delete():
    pass
