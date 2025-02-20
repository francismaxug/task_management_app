from pydantic import BaseModel, Field, EmailStr, WithJsonSchema, UUID4
from typing_extensions import Annotated
from datetime import datetime

class UserBase(BaseModel):
    name:str | None = Field(title="User name", description="This is the name assign oer user", default=None, max_length=20)
    email: Annotated[EmailStr, Field(strict=True, title="User name", description="This is the name assign oer user"), WithJsonSchema({'extra': 'data'})]
    password: Annotated[str, Field(strict=True), WithJsonSchema({'extra': 'data'})]
    
    
class User(UserBase):
    id: UUID4 = Field(title="ID", description="This is a unique identifier assigned to every user")
    token:str
    created_at: datetime = Field(title="Date created", description="Date in which the user was created")
    
    
class UserCreateSuccess(BaseModel):
    message: str = Field(default="User Created Successfully", description="Success message after a user succcesful creates account")
    date: User = Field(title="Data", description="Data returned to the user")
    
    
class UserGetSuccess(BaseModel):
    message: str = Field(default="User Created Successfully", description="Success message after a user succcesful creates account")
    date: list[User] = Field(title="Data", description="Data returned to the user")