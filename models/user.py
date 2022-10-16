#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage_t
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_t and storage_t == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete, delete-orphan',
                              backref='user')
        reviews = relationship('Review', cascade='all, delete, delete-orphan',
                               backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
