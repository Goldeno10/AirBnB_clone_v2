#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship




place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    if storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_l = []
            reviews = models.storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    review_l.append(review)
            return review_l

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_l = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenity_l.append(amenity)
            return menity_l
