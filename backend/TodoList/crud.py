from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from Users.model import User

from .model import TodoList
from .schemas import CreateTodoList, UpdateTodoList


async def read_todolist(
        user: User,
        db: AsyncSession
):
    select_todolist = select(TodoList).where(TodoList.user_id == user.id)
    result_todolist = await db.execute(select_todolist)
    todolist_model = result_todolist.scalars().all()
    return todolist_model


async def read_todolist_id(
        id: int,
        user: User,
        db: AsyncSession
):
    select_todolist = select(TodoList).where(TodoList.id == id).options(selectinload(TodoList.items))\
        .where(TodoList.user_id == user.id)
    result_todolist = await db.execute(select_todolist)
    todolist_model = result_todolist.scalars().first()
    if not todolist_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return todolist_model


async def create_todolist(
        data: CreateTodoList,
        user: User,
        db: AsyncSession
):
    todolist = TodoList(**data.dict())
    todolist.user_id = user.id
    db.add(todolist)
    await db.commit()
    model = await read_todolist_id(todolist.id, user, db)
    return model


async def update_todolist(
        id: int,
        data: UpdateTodoList,
        user: User,
        db: AsyncSession
):
    todolist = await read_todolist_id(id, user, db)
    items_ids = [item.id for item in todolist.items]

    if len(data.delete_item) != 0:
        for i in data.delete_item:
            if i in items_ids:
                todolist.items = [item for item in todolist.items if item.id != i]
        data.delete_item = None

    for key, value in data.dict(exclude_none=True).items():
        setattr(todolist, key, value)
    db.add(todolist)
    await db.commit()
    return todolist


async def delete_todolist(
        id: int,
        user: User,
        db: AsyncSession
):
    todolist = await read_todolist_id(id, user, db)
    await db.delete(todolist)
    await db.commit()
    return todolist
