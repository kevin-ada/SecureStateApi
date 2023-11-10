from typing import List

from pydantic import BaseModel, EmailStr, conint


class RegUser(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    name: str
    email: EmailStr


class Image(BaseModel):
    url: str


class RegPost(BaseModel):
    title: str
    description: str
    price: int
    address: str
    city: str
    state: str
    zipcode: str

    class Config:
        from_attributes = True



class ImageOut(BaseModel):
    url: str
    product: RegPost


class RegOut(RegPost):
    owner: UserOut
    images: List[Image]


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True


class DataToken(BaseModel):
    token_id: str

    class Config:
        from_attributes = True


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

    class Config:
        from_attributes = True
