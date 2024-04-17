from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = ["http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your project!"}


with open("C:/Users/green/Desktop/projects/projectw/testData.json") as f:
    todos = json.load(f)


@app.get("/todos", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.post("/todos", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": ["Todo added successfully"]}
