from fastapi import (
    APIRouter,
    Body,
    Depends,
    Request,
    Response,
    HTTPException,
    status,
    Header,
    HTTPException,
)
from fastapi.encoders import jsonable_encoder
from typing import List, Annotated, Optional
from operator import attrgetter
from datetime import datetime, timezone
from models.user import User, datetime_now
router = APIRouter()




@router.post(
    "/",
    response_description="Create a new user",
    status_code=status.HTTP_201_CREATED,
    response_model=[],
)
def create_user(
    request: Request,
    user: User = Body(...),
    Authorization: Optional[str] = Header(None),
):
    print(request.state.jwt_content)
    user = jsonable_encoder(user)
    user['createdBy'] = request.state.jwt_content['emp_code']
    user['updatedBy'] = request.state.jwt_content['emp_code']
    new_user = request.app.database["users"].insert_one(user)
    created_project = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    return created_project


@router.get(
    "/list", response_description="List all Users", response_model=List[User]
)
def list_users(request: Request):
    users = list(request.app.database["users"].find(limit=100))
    return users

