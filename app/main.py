from fastapi import FastAPI
from utils.logger import logger
from app.core.db  import database
from app.core.db import settings

from contextlib import asynccontextmanager

@asynccontextmanager

async def life_span(app:FastAPI):
    logger.debug(f"Starting the FastAPI application {app.title}")
    
    await database.connect()
    
    logger.info(f"Data basese conncted to {settings.DATBASE_URL}")