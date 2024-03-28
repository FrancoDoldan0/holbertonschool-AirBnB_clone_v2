#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    if storage_type == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
