#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), foriegnKey("cities.id"), nullable=False)
    user_id = Column(String(60), foriegnKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(60), default=0, nullable=False)
    number_bathrooms = Column(Integer(60), default=0, nullable=False)
    max_guest = Column(Integer(60), default=0, nullable=False)
    price_by_night = Column(Integer(60), default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
