from databases import Database
from app.core.config import settings

database  = Database(url=settings.DATABESE_URL, min_size=2, max_size=10 )