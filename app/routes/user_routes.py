from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreateSuccess, User, UserBase
from sqlalchemy import select, insert
from app.services.user import get_user_email,user_create
import logging
logger = logging.getLogger(__name__)

user_router = APIRouter()

@user_router.post("/create", response_model=UserCreateSuccess, status_code=201)
async def create_user(user:UserBase):
    """
    Create new user
    """
    
    logger.info("Create user endpoint hit!!!")
    
    try:
        user_exist = await get_user_email(email=user.email)
        print(user_exist)
    
        if user_exist:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "User already exist"
        )
            
            
        user:User = await user_create(user=user)
        
        logger.info(f"Successfully created user: {user}")
        
        return UserCreateSuccess(data = user)
    except HTTPException:
        raise

    except Exception as e:
        # Catch unexpected errors (e.g., database errors)
        print(e)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

        
    
    