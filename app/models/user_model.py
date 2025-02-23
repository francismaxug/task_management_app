from app.models.base import metadata
from sqlalchemy import Table, UUID, ForeignKey, String, Column, text, DateTime, func
from datetime import datetime


user_table = Table(
    "users",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")),
    Column("name", String(length=20),  default=None),
    Column("email", String, nullable=False, unique=True),
    Column("password", String, nullable=False),
    Column("createdAt", DateTime, server_default=text('CURRENT_TIMESTAMP'))
)