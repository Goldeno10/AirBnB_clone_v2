#!/usr/bin/python3i
""" Review module for the HBNB project """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.place import Place


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    if storage_t == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
