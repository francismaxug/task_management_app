from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from asgi_correlation_id import CorrelationIdMiddleware
from app.core.db  import database
from app.core.db import settings
from app.utils.logger import logger,  configure_logging
from contextlib import asynccontextmanager
from app.routes.user_routes import user_router
import logging
logger = logging.getLogger(__name__)


@asynccontextmanager

async def life_span(app:FastAPI):
    configure_logging()
    logger.info(f"Starting the FastAPI application {app.title}")
    
    await database.connect()
    
    logger.info(f"Database connected successfuly 🚀🚀🚀")
    yield
    await database.disconnect()
    
    logger.warning("Gracefully closing server")
    
    
app = FastAPI(
    lifespan=life_span,
    title="Task Management app",
    description="A simple fastapi server to manage task",
    version="1.0"
)

app.add_middleware(CorrelationIdMiddleware)

app.include_router(router=user_router, prefix="/user")

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"HTTPException: {exc.status_code} - {exc.detail}")
    return await http_exception_handler(request, exc)