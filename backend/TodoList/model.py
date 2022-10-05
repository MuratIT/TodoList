from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class TodoList(Base):
    __tablename__ = "todolist"
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    user_id = Column(Integer, ForeignKey('user.id'))
    items = relationship("Item", cascade="all, delete-orphan")


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    descriptions = Column(Text)
    todolist_id = Column(Integer, ForeignKey('todolist.id'))
