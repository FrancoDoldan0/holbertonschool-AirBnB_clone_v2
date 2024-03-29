#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE')No se ha podido resolver la importación "sqlalchemy"


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if storage_type == 'db':

        places = relationship('Place', backref='user',
                              cascade='all, delete-orphan')

        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
