from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    document: int
    pis: int
    password: str
    zipcode: int
    address: str
    number: int
    complement: str
    city: str
    state: str
    country: str
