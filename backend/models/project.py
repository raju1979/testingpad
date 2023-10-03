import uuid
from typing import Optional
from pydantic import BaseModel, Field, constr
from pydantic.functional_validators import AfterValidator
from datetime import datetime, timezone
from bson import ObjectId as _ObjectId

def datetime_now() -> datetime:
    print(datetime.now(tz=timezone.utc).replace(microsecond=0))
    return datetime.now(tz=None)

class Project(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(constr(max_length=30))
    description: str = Field(constr(max_length=200))
    createdAt: datetime = Field(default_factory=datetime_now)
    updatedAt: datetime = Field(default_factory=datetime_now)
    createdBy: Optional[str] = None
    updatedBy: Optional[str] = None
    archived: Optional[bool] = False
    deleted: Optional[bool] = False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": { 
                "title": "Don Quixote",
                "description": "This is a description of project"
            }
        }

class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(constr(max_length=30))
    description: Optional[str] = Field(constr(max_length=200))
    archived: Optional[bool] = False
    deleted: Optional[bool] = False
    
    class Config:
        schema_extra = {
           "example": { 
                "title": "Don Quixote",
                "description": "This is a description of project"
            }
        }