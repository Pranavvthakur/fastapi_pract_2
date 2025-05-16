from fastapi import FastAPI, Depends
import blog.schemas as schemas
import blog.models as models
from blog.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from blog.routers import blog
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)

@app.post('/blog', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.blog(title=request.title, body=request.body)
    db.add(new_blog)

    db.commit() 
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.blog).all()
    return blogs


@app.get('/blog/{id}')
def shoe(id, db: Session = Depends(get_db)):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        return {'error': 'Blog not found'}
    return blog

