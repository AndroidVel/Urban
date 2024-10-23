from module_17.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from module_17.app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')

    tasks = relationship('Task', back_populates='user')
