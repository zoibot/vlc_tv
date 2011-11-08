from sqlalchemy import create_engine

import schedule, series, episode, clip

import base

engine = create_engine("sqlite:///test.db")
print engine
base.Base.metadata.create_all(engine)
