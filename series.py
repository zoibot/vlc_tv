from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey

from base import Base

from episode import Episode

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    episodes = relationship("Episode")
    name = Column(String)
    seasons = Column(Integer)
    start_year = Column(Integer)
    end_year = Column(Integer)
    image = Column(LargeBinary)
