from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import uvicorn



app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int = Field(..., gt=0, le=120)  # age must be greater than 0 and less than or equal to 120

# @app.post("/users/")
# def create_user(user:User):
#     return {"name": user.name, "age": user.age}

# @app.get("/users/{name}")
# def read_user(name: str):
#     return {"name": name, "message": "User found", }    




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return {'data': f"My Item name is {item.name }"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9000)


    