from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    document = Column(Integer)
    pis = Column(Integer)
    password = Column(String)
    zipcode = Column(Integer)
    address = Column(String)
    number = Column(Integer)
    complement = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
