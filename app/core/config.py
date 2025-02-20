from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from enum import Enum

class ENVIRONMENT(str, Enum):
    DEVELOPMENT="development"
    PRODUCTION="production"
    TEST="testing"
    
    
class Settings(BaseSettings):
    ENVIRONMENT:str = ENVIRONMENT.DEVELOPMENT
    DATABASE_URL:str = Field( title="Postgres databse url", description="The connection string to connect to your database")
    ALEMBIC_DATABASE_URL:str = Field( title="Alembi databse url", description="The connection string to connect to your alembic")
    APP_NAME:str
    JWT_SECRETE:str
    ACCESS_TOKEN_EXPIRE_MINUTES:str
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_ignore_empty=True
    )
    

    
    
settings = Settings() #type :igore