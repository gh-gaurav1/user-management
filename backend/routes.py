from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
from crud import get_user, get_users, create_user, update_user, delete_user
from schema import User, UserCreate
from fastapi.responses import RedirectResponse

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users    

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=User)
def update_existing_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/users/{user_id}", response_model=User)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)

@router.get("/")
def root():
    return RedirectResponse(url="/docs")  # Return the RedirectResponse object