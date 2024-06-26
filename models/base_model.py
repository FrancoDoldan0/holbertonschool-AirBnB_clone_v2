#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs or 'updated_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()

            for name, value in kwargs.items():
                if name == 'created_at' or name == 'updated_at':
                    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, date)
                else:
                    if name != '__class__' and name in dir(self):
                        setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Deletes the instance from storage """
        models.storage.delete(self)
