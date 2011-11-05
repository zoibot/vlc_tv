from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

from clip import Clip

class Episode(Base):
        __tablename__ = 'clips'
        id = Column(Integer, primary_key=True)
        clips = relationship("Clip")
