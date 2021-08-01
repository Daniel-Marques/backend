from datetime import datetime, time, timezone
from sqlalchemy import Column, Integer, String, DateTime
from src.infra.sqlalchemy.config.database import Base, create_db

class UserModel(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    document = Column(String)
    pis = Column(String)
    email = Column(String)
    password = Column(String)
    zipcode = Column(Integer)
    address = Column(String)
    number = Column(Integer)
    complement = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True))
