from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    document: str
    pis: str
    email: str
    password: Optional[str]
    zipcode: int
    address: str
    number: Optional[int]
    complement: Optional[str]
    city: str
    state: str
    country: str
    created_at: Optional[str]
    updated_at: Optional[str]


class UserWithoutPasswordSchema(BaseModel):
    id: Optional[str]
    name: str
    document: str
    pis: str
    email: str
    password: Optional[str]
    zipcode: int
    address: str
    number: Optional[int]
    complement: Optional[str]
    city: str
    state: str
    country: str
    created_at: Optional[str]
    updated_at: Optional[str]


class UserOut(BaseModel):
    id: Optional[str]
    name: str
    document: str
    pis: str
    email: str
    password: Optional[str]
    zipcode: int
    address: str
    number: Optional[int]
    complement: Optional[str]
    city: str
    state: str
    country: str
    created_at: Optional[str]
    updated_at: Optional[str]


class UserSimpleSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    email: str
    password: str


class LoginSuccessSchema(BaseModel):
    user: UserSimpleSchema
    access_token: str


class UserSignupSchema(BaseModel):
    id: Optional[str]
    name: str
    document: Optional[str]
    pis: Optional[str]
    email: str
    password: str
    zipcode: Optional[int]
    address: Optional[str]
    number: Optional[int]
    complement: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]

class SignupSuccessSchema(BaseModel):
    user: UserSimpleSchema
    access_token: str
