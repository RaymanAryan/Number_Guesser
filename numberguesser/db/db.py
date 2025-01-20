import sqlalchemy.orm
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Base class for SQLAlchemy models
Base = sqlalchemy.orm.declarative_base()

# Define the GameData model
class GameData(Base):
    __tablename__ = 'game_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    target_number = Column(Integer, nullable=False)
    attempts = Column(Integer, nullable=False)
    range_limit = Column(Integer, nullable=False)
    date_played = Column(DateTime, default=datetime.now)

# Database setup

if not os.path.exists("guess_game.db"):
    engine = create_engine('sqlite:///guess_game.db', echo=False)
    Base.metadata.create_all(engine)  # Ensure tables are created
engine = create_engine('sqlite:///guess_game.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def save_game_data(target_number, attempts, range_limit):
    new_game = GameData(
        target_number=target_number,
        attempts=attempts,
        range_limit=range_limit
    )

    session.add(new_game)  # Add to the session
    session.commit()       # Commit the transaction
    print("Game data saved successfully!")



def get_all_game_data():
    # Retrieve all game records from the database
    games = session.query(GameData).all()

    for game in games:
        print(f"Game ID: {game.id}, Target: {game.target_number}, Attempts: {game.attempts}, Range Limit: {game.range_limit}, Date: {game.date_played}")

# Example usage
get_all_game_data()


