from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int
    email: str
    f_name: str
    l_name: str
    presentation: Optional[str] = Field(max_length=512, default="")# needs max len 512 and default: (see ref. page --> schema 'User')

    class Config():
        orm_mode=True

        
class UserCreate(BaseModel):
    email: str
    f_name: str
    l_name: str

    class Config():
        orm_mode=True

class UserDelete(BaseModel):
    email: str

    class Config():
        orm_mode=True