from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas

# GET /health
def health_check():
    return {"status": "ok"}

# GET /users 
def get_users(db: Session, role: str | None = None):
    query = db.query(models.Users)

    if role:
        query = query.filter(models.Users.role == role)

    return query.all()

# GET /users/{id}
def get_user_by_id(user_id: int, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

# POST /users
def create_user(user: schemas.UserCreate, db: Session):
    existing_user = db.query(models.Users).filter(
        models.Users.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
