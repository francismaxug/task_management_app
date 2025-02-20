from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import ForeignKey, UUID
import uuid

Base = declarative_base()

# Import the tables from their respective files
from app.models.user_model import user_table
from app.models.tasks_model import  task_table


class User(Base):
    __table__ = user_table

    # Relationship to tasks where the user is assigned
    assigned_tasks = relationship("Task", foreign_keys="Task.assignedTo", back_populates="assignee")

    # Relationship to tasks where the user is the creator
    created_tasks = relationship("Task", foreign_keys="Task.createdBy", back_populates="creator")

class Task(Base):
    __table__ = task_table

    # Relationship to the user who is assigned the task
    assignee = relationship("User", foreign_keys="User.id", back_populates="assigned_tasks")

    # Relationship to the user who created the task
    creator = relationship("User", foreign_keys="User.id", back_populates="created_tasks")