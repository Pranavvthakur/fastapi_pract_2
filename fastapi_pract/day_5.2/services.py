from models import User
from db import SessionLocal

def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()