#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nulleable = False)
    user_id = Column(String(60), ForeignKey('users.id'), nulleable = False)
    name = Column(String(128), nulleable = False)
    description = Column(String(1024), nulleable = True)
    number_rooms = Column(Integer, nulleable = False, default = 0)
    number_bathrooms = Column(Integer, nulleable = False, default = 0)
    max_guest = Column(Integer, nulleable = False, default = 0)
    price_by_night = Column(Integer, nulleable = False, default = 0)
    latitude = Column(Float, nulleable = True)
    longitude = Column(Float, nulleable = True)
    amenity_ids = []
