from fastapi import FastAPI
from todo.todo import todo_router

app = FastAPI()

@app.get("/")
async def wellcome() -> dict:
    return {"message": "Hello World!"}

app.include_router(todo_router)