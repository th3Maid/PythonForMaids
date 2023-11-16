from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        Schema_extra: {
            "Example": {
                "item": "Some string item"
            }
        }


# Nested Models
class Item(BaseModel):

    item: str
    status: str

class NestedTodo(BaseModel):
    id: int
    item: Item

