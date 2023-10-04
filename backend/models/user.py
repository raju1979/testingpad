import uuid
from typing import Optional
from pydantic import BaseModel, Field, constr
from pydantic.functional_validators import AfterValidator
from datetime import datetime, timezone
from bson import ObjectId
from typing_extensions import Annotated

from models.PyObjectId import PyObjectId
from pydantic import BaseModel, Field as PydanticField

def check_object_id(value: str) -> str:
    if not ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


ObjectId = Annotated[str, AfterValidator(check_object_id)]

def datetime_now() -> datetime:
    print(datetime.now(tz=timezone.utc).replace(microsecond=0))
    return datetime.now(tz=None)

class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(constr(max_length=30))
    firstName: str = Field(constr(max_length=30))
    lastName: str = Field(constr(max_length=30))
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
                "username": "rdhoundiyal",
                "firstName": "Rajesh",
                "lastName": "Dhoundiyal"
            }
        }