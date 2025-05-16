from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning 1"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "Deep Learning 2"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "Deep Learning 3x"}
    return {"model_name": model_name, "message": "Model not found"}   



@app.get("/")
def read_root():
    return {"message": "Hello World"}

#query parameter example
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


#path parameter example
@app.get("/items/{item_id}/name/{item_name}")
def read_item(item_id: int, item_name: str):
    return {"item_id": item_id, "item_name": item_name} 

@app.get("/items/")
def read_items(name: str, price: int):
    return {"name": {name}, "price": {price}}
@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted"}