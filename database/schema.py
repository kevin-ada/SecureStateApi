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


class RegPost(BaseModel):
    title: str
    description: str
    image:str
    price: int
    address: str
    city: str
    state: str
    zipcode: str

    class Config:
        from_attributes = True


class RegOut(RegPost):
    owner: UserOut


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
