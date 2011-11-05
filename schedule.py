from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

from series import Series

class ScheduleBlock(Base):
    __tablename__ = 'schedblocks'
    id = Column(Integer, primary_key=True)
    time = Column(String)
    series = relationship("Series")
    series_id = Column(Integer, ForeignKey('series.id'))
