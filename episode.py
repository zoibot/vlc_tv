from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from base import Base

from clip import Clip

class Episode(Base):
        __tablename__ = 'episodes'
        id = Column(Integer, primary_key=True)
        series_id = Column(Integer, ForeignKey('series.id'))
        name = Column(String)
        season = Column(Integer)
        number = Column(Integer)
        clips = relationship("Clip")
