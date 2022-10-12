#!/usr/bin/python3
"""
"""


from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DbStorage:
    """
    """
    __engine = None
    __session = None
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine  = ("mysql+mysqldb://{}:{}@{}/{}".\
                format(user, passwd, host, db),
                pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)


