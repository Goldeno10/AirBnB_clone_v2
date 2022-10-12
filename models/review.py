#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlachemy import Column, String
from models.place import Place
from models.review import Review



class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), foreignKey('place.id'), nulable=False)
    user_id = Column(String(60), foreignKey('user.id'), nulable=False)
    text = Column(String(1024), nulable=False)
