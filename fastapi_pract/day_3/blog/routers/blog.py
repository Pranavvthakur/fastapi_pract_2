from typing import List
from fastapi import APIRouter, Depends
import blog.schemas as schemas
from blog.database import get_db
from blog.models import blog
from sqlalchemy.orm import Session
router = APIRouter()

@router.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(blog).all()
    return blogs