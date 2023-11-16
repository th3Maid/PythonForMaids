from fastapi import APIRouter, Path
from todo.model import Todo, NestedTodo, TodoItem

todo_router = APIRouter()

todo_list = []
nested_todo = []

@todo_router.get("/todo")
async def retrive_todo() -> dict:
    return {
        "todos": todo_list
    }

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "status": "Ok",
        "todo": todo
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of todo to retrive")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    
    return {
        "todo": "todo ID not found"
    }

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="Update todo ID")) -> dict:

    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated"
            }

    return {
        "message": "Todo supplied ID doesn't exist"
    }

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int) -> dict:

    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted"
            }

    return {
        "message": "Todo supplied ID doesn't exist"
    }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:

    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }


@todo_router.get("/nested/todo")
async def retrive_nested_todo() -> dict:
    return {
        "nested_todos": nested_todo
    }

@todo_router.post("/nested/todo")
async def add_nested_todo(todo: NestedTodo) -> dict:
    nested_todo.append(todo)
    return {
        "status": "Ok",
        "nested_todo": todo
    }

# Exemple of nested todo
# {
#     "id": 4,
#     "item": {
#         "item": "Some item",
#         "status": "true"
#     }
# }

