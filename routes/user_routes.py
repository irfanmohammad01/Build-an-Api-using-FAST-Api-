from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Annotated

import schemas
from database import SessionLocal
from controllers import user_controller

router = APIRouter(tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# GET /health
@router.get("/health", status_code=200)
def health():
    return user_controller.health_check()

# GET /users
@router.get("/users", response_model=List[schemas.UserResponse])
def get_users(
    db: db_dependency,
    role: str | None = Query(default=None)
):
    return user_controller.get_users(db, role)

# GET /users/{id}
@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: db_dependency):
    return user_controller.get_user_by_id(user_id, db)

# POST /users
@router.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: db_dependency):
    return user_controller.create_user(user, db)
