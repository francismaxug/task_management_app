from sqlalchemy import Table, String, DateTime, UUID, ForeignKey, text, Column, Text, Enum

from app.models.base import metadata

from app.schemas.tasks import TASK_STATUS, PRIORITY


task_table = Table(
    "tasks",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")),
    Column("title", String(100),  nullable=False),
    Column("description", Text(), nullable=False),
    Column("status", Enum(TASK_STATUS), default=TASK_STATUS.OPEN),
    Column("priority",Enum(PRIORITY), default=PRIORITY.LOW),
    Column("assignedTo", UUID(as_uuid=True), ForeignKey("users.id")),  # Foreign key to user
    Column("createdBy", UUID(as_uuid=True), ForeignKey("users.id")),  # Foreign key to user
)