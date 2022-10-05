from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    todolist = relationship("TodoList", cascade="all, delete-orphan")
