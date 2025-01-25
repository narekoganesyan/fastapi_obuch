import uvicorn
from pydantic import EmailStr, BaseModel
from fastapi import FastAPI

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr

@app.get("/hello/")
async def hello(name: str, surname: str) -> dict:
    name = name.strip().title()
    surname = surname.strip().title()
    return {"message": f"Привет, {name} {surname}! Ты на главной странице"}


@app.post("/users/")
async def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }

@app.post("/calc/add/")
async def add_calc_add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/items/latest/")
async def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return {
        "item":
            {
                "id": item_id,
            }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
