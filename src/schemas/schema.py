from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    document: str
    pis: str
    email: str
    password: str
    zipcode: int
    address: str
    number: Optional[int]
    complement: Optional[str]
    city: str
    state: str
    country: str
    created_at: Optional[str]
    updated_at: Optional[str]
