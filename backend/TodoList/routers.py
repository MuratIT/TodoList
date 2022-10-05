from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
from Users.users import current_active_user, User
from .schemas import CreateTodoList, UpdateTodoList, ReadTodoList, ReadAllTodoList
from .crud import create_todolist, update_todolist, delete_todolist, read_todolist, read_todolist_id

router = APIRouter(
    prefix='/todolist',
    tags=['TodoList'],
    dependencies=[Depends(current_active_user)]
)


@router.get('/', response_model=List[ReadAllTodoList])
async def todolist(
        user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session)
):
    return await read_todolist(user, db)


@router.post('/create', response_model=ReadTodoList)
async def todolist_create(
        create_todo_list: CreateTodoList,
        user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session)
):
    return await create_todolist(create_todo_list, user, db)


@router.get('/{id}', response_model=ReadTodoList)
async def todolist_id(
        id: int,
        user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session)
):
    return await read_todolist_id(id, user, db)


@router.patch('/update/{id}', response_model=ReadTodoList)
async def todolist_update(
        id: int,
        update_todo_list: UpdateTodoList,
        user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session)
):
    return await update_todolist(id, update_todo_list, user, db)


@router.delete('/delete{id}', response_model=ReadTodoList)
async def todolist_delete(
        id: int,
        user: User = Depends(current_active_user),
        db: AsyncSession = Depends(get_async_session)
):
    return await delete_todolist(id, user, db)


