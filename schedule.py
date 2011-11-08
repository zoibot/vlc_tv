from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from base import Base

from series import Series

class ScheduleBlock(Base):
    __tablename__ = 'schedblocks'
    id = Column(Integer, primary_key=True)
    time = Column(String)
    series_id = Column(Integer, ForeignKey('series.id'))
    series = relationship("Series")
