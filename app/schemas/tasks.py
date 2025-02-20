from pydantic import BaseModel, Field, UUID4, WithJsonSchema
from typing_extensions import Annotated
from datetime import datetime, timedelta
from enum import Enum

class TASK_STATUS(str, Enum):
    OPEN= "Open"
    IN_PROGRES= "In_Progress"
    COMPLETED= "Completed"
    
    
class PRIORITY(str, Enum):
    LOW= "Low"
    HIGH= "High"
    MEDIUM= "Medium"


def calculate_end_date(start_date: str) -> str:
    start_date_obj = datetime.fromisoformat(start_date)
    end_date_obj = start_date_obj + timedelta(days=90)  # Approximate 3 months
    return end_date_obj.isoformat()


class TaskBaseSchema(BaseModel):
    title:  Annotated[str,Field(title="Title", description="Title of the task", min_length=3, max_length=50, strict=True, ),  WithJsonSchema({'extra': 'data'}) ] 
    description: str = Field(title="Description", description="Description of the task", min_length=3, max_length=500, default=""),
    status : Annotated[TASK_STATUS,Field(title="Status", description="Status of the task", default=TASK_STATUS.OPEN, strict=True),  WithJsonSchema({'extra': 'data'}) ] 
    start_date: str = Field(title="Start Date", description="Start date of the task", default_factory=lambda: datetime.now().isoformat())   
    end_date: str = Field(title="End Date", description="End date of the task",  default_factory=lambda: calculate_end_date(datetime.now().isoformat()) )
    assignedTo: UUID4 = Field(title="Assigned To", description="User assigned to the task")
    createdBy: UUID4 = Field(title="Created By", description="User who created the task")
    priority: Annotated[PRIORITY , Field(title="Priority", description="Priority of the task", default=PRIORITY.LOW), WithJsonSchema({'extra': 'data'})]
    
    
class Task(TaskBaseSchema):
    id:UUID4
    created_at: datetime = Field(title="Date created", description="This is the date the task got created", default=None)
    
    
class SuccessCreateTaskResponse(BaseModel):
    message:str = Field(title="Message", description="Message to be delivered after creation of task", default="Task Created Successfully")
    
    data: Task = Field(title="Data", description="Single task data")
    
    
    
class SuccessGestTaskResponse(BaseModel):
    
    message:str = Field(title="Message", description="Message to be delivered after a get request", default="Success")
    
    data: list[Task] = Field(title="Data", description="One or more task data")