#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import ForeignKey

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), foreignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place",
            cascade='all, delete, delete-orphan',
            backref="cities")
=======
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if storage_t and storage_t == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                              backref="cities")
    else:
        state_id = ""
        name = ""
>>>>>>> a5af9a6d679eecac472d160f2138ad01b7d91fb2
