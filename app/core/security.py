import jwt
from passlib.context import CryptContext

from datetime import timezone, datetime, timedelta

from app.core.config import settings

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_access_token(data:str)->str:
    """
    creates access token
    
    """
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode = {"exp": expire, "sub":data}
    encoded_jwt = jwt.encode(payload=to_encode, key=settings.JWT_SECRETE, algorithm=ALGORITHM)
    return encoded_jwt


def hashed_password(password) ->str:
   """
   hash the users password
   """
   return pwd_context.hash(secret=password)
    
    

def check_password(raw_password:str, hashed_password)->bool:
    """_summary_

    Args:
        raw_password (str):
        hashed_password (bool):

    Returns:
        bool
    """
    return pwd_context.verify(secret=raw_password, hash=hashed_password)


