#!/usr/bin/python3
""" Contains the DbStorage class for database storage """


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
    """ A database Storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize variables """
        user = ( "HBNB_MYSQL_USER")
        passwd = ("HBNB_MYSQL_PWD")
        db = ("HBNB_MYSQL_DB")
        host = ("HBNB_MYSQL_HOST")
        env = ("HBNB_ENV")
        self.__engine = ("mysql+mysqldb://{}:{}@{}/{}".
                         format(user, passwd, host, db),
                         pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        self__.session = Session()
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        cls_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        dic = {}
        if not cls:
            for i in cls_list:
                obj = self.__session.query(i).all()
                key = f'{i}.{obj}'
                dic[key] = obj
        else:
            obj = self.__session.query(i).all()
            key = f'{i}.{obj}'
            dic[key] = obj
        return (dic)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.engine,
                               expire_on_commit=False)
        sess_scope = scoped_session(session)
        self.__session(sess_scope)
