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
from models.project import Project, ProjectUpdate, datetime_now
router = APIRouter()




@router.post(
    "/",
    response_description="Create a new project",
    status_code=status.HTTP_201_CREATED,
    response_model=[],
)
def create_project(
    request: Request,
    project: Project = Body(...),
    Authorization: Optional[str] = Header(None),
):
    print(request.state.jwt_content)
    project = jsonable_encoder(project)
    project['createdBy'] = request.state.jwt_content['emp_code']
    project['updatedBy'] = request.state.jwt_content['emp_code']
    new_project = request.app.database["projects"].insert_one(project)
    created_project = request.app.database["projects"].find_one(
        {"_id": new_project.inserted_id}
    )
    return created_project


@router.get(
    "/list", response_description="List all Projects", response_model=List[Project]
)
def list_projects(request: Request):
    projects = list(request.app.database["projects"].find(limit=100))
    return projects


@router.put("/{id}", response_description="Update a Project", response_model=Project)
def update_project(id: str, request: Request, project: ProjectUpdate = Body(...)):

    existing_project = request.app.database["projects"].find_one({"_id": id})
    print('existing_project', existing_project)
    if not existing_project:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # updatedAt, updatedBy = attrgetter('updatedAt', 'updatedBy')(existing_project)

    project = jsonable_encoder(project)
    print('project', project)
    # project["updatedAt"] = datetime.now(tz=None)
    # project["updatedBy"] = request.state.jwt_content['emp_code']

    project_temp = {
        "title": "hello world",
        "updatedAt": datetime.now(tz=None),
        "updatedBy": request.state.jwt_content['emp_code']
    }
    project_temp = jsonable_encoder(project_temp)

    update = {"$set": project_temp}
    print(update)

    result = request.app.database["projects"].update_one({"_id": id}, update)

    # if result.modified_count == 1:
    #     return {"message": "Document updated successfully"}
    # else:
    #     return {"message": "No documents updated"}


    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"project with ID {id} not found")



@router.get("/{id}", response_description="Get a single project by id", response_model=Project)
def find_book(id: str, request: Request):
    if (project := request.app.database["projects"].find_one({"_id": id})) is not None:
        return project
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"project with ID {id} not found")