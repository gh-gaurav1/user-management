# crud.py
from sqlalchemy.orm import Session
from models import User
from schema import UserCreate
import logging

logger = logging.getLogger(__name__)

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    logger.info("Creating a new user with username: %s", user.username)
    db_user = User(username=user.username, password=user.password, age=user.age, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserCreate):
    logger.info("Updating user with id: %d", user_id)
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.password = user.password
        db_user.age = user.age
        db_user.phone_number = user.phone_number
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    logger.info("Deleting user with id: %d", user_id)
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
