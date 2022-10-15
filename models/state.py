#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    if storage_t and storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

        @property
        def cities(self):
            all_c = models.storage.all()
            list_c = []
            result = []
            for key in all_c:
                city = key.split('.')
                if (city[0] == 'City'):
                    lista.append(all_c[key])
            for item in list_c:
                if (item.state_id == self.id):
                    result.append(item)
            return (result)
    else:
        name = ""
