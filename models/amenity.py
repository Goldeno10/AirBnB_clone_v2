#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Create the amenities """
    __tablename__ = 'amenities'
    if storage_t and storage_t == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
