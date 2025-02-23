from sqlalchemy import select, insert
from app.models.user_model import user_table
from app.core.db import database
from app.schemas.user import User, UserBase
from app.core.security import hashed_password, create_access_token
from pydantic import UUID4


async def get_user_email(email:str)-> User | None:
    query = select(user_table).where(user_table.c.email == email)
    user  = await database.fetch_one(query=query)
    
    return user



async def user_create(user:UserBase):
    hash_p = hashed_password(password=user.password)
    
    data = user.model_dump(exclude={"password"})
    
    query = insert(user_table).values(
        **data,
        password=hash_p
    )
    
    id:UUID4 = await database.execute(query=query)
    
    token = create_access_token(data=user.email)
    
    return User(id=id, token=token, **vars(user))