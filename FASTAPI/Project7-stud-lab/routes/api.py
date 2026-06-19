from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.models import User, Post
from schemas.userschema import UserSchema, PostCreate
from database.config import get_db

router = APIRouter(prefix="/userpost")


@router.get("/", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).options(joinedload(User.posts)).all()


@router.post("/", response_model=UserSchema)
def add_user(data: UserSchema, db: Session = Depends(get_db)):
    user = User(
        name=data.name,
        email=data.email,
        course=data.course,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/post")
def create_post(data: PostCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    post = Post(
        title=data.title,
        user_id=data.user_id
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@router.get("/{user_id}/posts", response_model=List[PostCreate])
def users_posts(user_id: int, db: Session = Depends(get_db)):
    posts = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .all()
    )

    if not posts:
        raise HTTPException(status_code=404, detail="No posts found")

    return posts