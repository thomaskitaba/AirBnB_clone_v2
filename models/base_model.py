#!/usr/bin/python3
""" Define base model class that contains information
that is shared by all classes"""
import os
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """The base model class"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            # if os.getenv('HBNB_TYPE_STORAGE') in ('db'):
            if not hasattr(kwargs, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(kwargs, 'created_at'):
                setattr(self, 'created_at', datetime.now())
            if not hasattr(kwargs, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """Deletes a specfic instance from the storage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """Update updated_at attribute """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert Object into dict format"""
        temp = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    temp[key] = value.isoformat()
                else:
                    temp[key] = value
        temp['__class__'] = self.__class__.__name__
        return (temp)
