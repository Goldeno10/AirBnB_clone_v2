#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
            cascade='all, delete, delete-orphan',
            backref="state")

    @property
    def cities(self):
        dic = models.storage.all()
        dict_key = []
        result = []
        for key in dic:
            city = key.split('.')
            if city[0] == 'City':
                dict_key.append(dic[key])
        for item in dict_key:
            if (item.state_id == self.id):
                result.append(item)
        return (result)

