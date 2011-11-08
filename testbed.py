from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import schedule, series, episode, clip

e = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=e)

Sr = series.Series
Sc = schedule.ScheduleBlock
Ep = episode.Episode
Clip = clip.Clip

