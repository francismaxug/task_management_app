import logging

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M", filename="app.log")

# Create a logger instance
logger = logging.getLogger(__name__)