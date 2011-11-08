from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from base import Base

class Clip(Base):
        __tablename__ = 'clips'
        id = Column(Integer, primary_key=True)
        episode_id = Column(Integer, ForeignKey('episodes.id'))
        file_name = Column(String)
        start_time = Column(String)
        end_time = Column(String)
