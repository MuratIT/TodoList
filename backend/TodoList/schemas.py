import re
from typing import List, Optional

from pydantic import BaseModel, validator

from fastapi import HTTPException, status


class ItemTodoList(BaseModel):
    class Config:
        orm_mode = True


class ReadItemTodoList(ItemTodoList):
    id: int
    title: str
    descriptions: str


class TodoList(BaseModel):
    title: Optional[str]

    @validator('title')
    def title_len(cls, v):
        if len(v) > 150 or len(v) == 0 or re.search(r'^\s|\s$', v):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return v

    class Config:
        orm_mode = True


class CreateTodoList(TodoList):
    pass


class ReadTodoList(TodoList):
    id: int
    items: List[ReadItemTodoList] = []


class ReadAllTodoList(TodoList):
    id: int


class UpdateTodoList(TodoList):
    delete_item: List[int] = []
