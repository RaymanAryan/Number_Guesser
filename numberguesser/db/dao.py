# Save game data

from db import *

def save_game_data(target_number, attempts, range_limit):
    new_game = GameData(
        target_number=target_number,
        attempts=attempts,
        range_limit=range_limit
    )
    session.add(new_game)
    session.commit()
    print("Game data saved successfully!")