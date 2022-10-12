#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlachemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy.orm import relatonship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(Strimg(128), nulladble=False)
    password = Column(Strimg(128), nulladble=False)
    first_name = Column(Strimg(128), nulladble=False)
    last_name = Column(Strimg(128), nulladble=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')
    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')
