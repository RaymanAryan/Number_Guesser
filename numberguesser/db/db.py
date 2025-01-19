from datetime import datetime

import sqlalchemy.orm
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy setup
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy setup
Base = sqlalchemy.orm.declarative_base()

class GameData(Base):
    __tablename__ = 'game_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    target_number = Column(Integer, nullable=False)
    attempts = Column(Integer, nullable=False)
    range_limit = Column(Integer, nullable=False)
    date_played = Column(DateTime, default=datetime.now)

# Database initialization
engine = create_engine('sqlite:///guess_game.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()