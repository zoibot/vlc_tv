from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Blob, ForeignKey

Base = declarative_base()

from episode import Episode

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    episodes = relationship("Episode")
    name = Column(String)
    seasons = Column(Integer)
    start_year = Column(Integer)
    end_year = Column(Integer)
    image = Column(Blob)
