import logging

from app.core.config import settings


from logging.config import dictConfig

from logging.config import dictConfig
from typing import Dict, Any


def obfuscated_email(email: str, obfuscation_length: int) -> str:
    characters = email[ : obfuscation_length]
    first, last = email.split("@")
    return characters + ("*" * (len(first) - obfuscation_length)) + "@" + last
  

class EmailObfuscationFilter(logging.Filter):
    def __init__(self, name = "", obfuscation_length = 4, obfuscation_char = "*"):
        super().__init__(name)
        self.obfuscation_length = obfuscation_length
        
        def filter(self, record: logging.LogRecord) -> bool:
            if "email" in record.__dict__:
                record.email = obfuscated_email(record.email, self.obfuscation_length)
            return True

def configure_logging() -> None:
    logging_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        'filters': {
      'correlation_id': {
         '()': 'asgi_correlation_id.CorrelationIdFilter',
           'uuid_length': 12 if settings.ENVIRONMENT == "development" else 32,
          'default_value': '-', 
      },
      
        'email_obfuscation': {
            "()": EmailObfuscationFilter,
            "obfuscation_length": 3 if settings.ENVIRONMENT == "development" else 0
        }
      },
        "formatters": {
            "console": {
                "class": "logging.Formatter",
                "datefmt": "%Y-%m-%d %H:%M",
                "format": " [%(correlation_id)s] %(name)s:%(lineno)d - %(message)s"
            },
            #USING NORMAL STRING LOGGING
             "file": {
                "class": "logging.Formatter",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "format": "[%(asctime)s.%(msecs)03dZ] | [%(levelname)-8s] | [%(correlation_id)s] | %(name)s:%(lineno)d - %(message)s"
            }
            
            
            #USING PYTHON-LOGGER MODULE
            # "file": {
            #     "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            #     "datefmt": "%Y-%m-%d %H:%M:%S",
            #     "format": "%(asctime)s.%(msecs)03d %(levelname)-8s %(correlation_id)s %(name)s:%(lineno)d - %(message)s"
            # }
        },
        "handlers": {
            "default": {
                "class": "rich.logging.RichHandler",
                "level": "DEBUG",
                'filters': ['correlation_id'],
                "formatter": "console"
            },
            "rotating_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "file",
                "filename": "taskapp.log",
                "maxBytes": 1024 * 1024 * 1,  # 1MB
                "backupCount": 5,
                "encoding": "utf8",
                'filters': ['correlation_id'],
            }
        },
        "loggers": {
            # FastAPI and related loggers
            "fastapi": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False
            },
            "uvicorn": {
                "handlers": ["default", "rotating_file"],
                "level": "INFO"
            },
            "uvicorn.access": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False
            },
            "uvicorn.error": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False
            },
            # Database loggers
            "postgresql": {
                "handlers": ["default"],
                "level": "INFO"
            },
            "databases": {
                "handlers": ["default"],
                "level": "INFO"
            },
            # Your application logger
            "app": {
                "handlers": ["default", "rotating_file"],
                "level": "DEBUG",
                "propagate": False
            },
            # Additional common loggers
            "sqlalchemy": {
                "handlers": ["default"],
                "level": "WARNING",
                "propagate": False
            },
            "gunicorn": {
                "handlers": ["default"],
                "level": "INFO",
                "propagate": False
            },
          
        }
    }
    
    dictConfig(logging_config)
    
    
logger = logging.getLogger(__name__)