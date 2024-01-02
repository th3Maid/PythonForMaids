from fastapi import APIRouter
from models import Todo
todo_router = APIRouter()


todos_list = [
		{
            "id": 1,
            "item": "Hello world"
        },
        {
            "id": 2,
            "item": "Hello world"
        },
        {
            "id": 3,
            "item": "Hello world"
        },
        {
            "id": 4,
            "item": "Hello world"
        },
        {
            "id": 5,
            "item": "Hello world"
        }
]






@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
	todos_list.append(todo)
	return {
		"message": "Todo add successfully"
	}

@todo_router.get("/todo")
async def get_todos() -> dict:
	return {
		"todos": todos_list 
	}
