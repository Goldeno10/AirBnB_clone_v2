#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_t, storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The State class """
    if storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            all_c = storage.all()
            list_c = []
            result = []
            for key in all_c:
                city = key.split('.')
                if (city[0] == 'City'):
                    list_c.append(all_c[key])
            for item in list_c:
                if (item.state_id == self.id):
                    result.append(item)
            return (result)
