import os

from dotenv import load_dotenv

load_dotenv()

LIVES = os.getenv('LIVES')
RATING = os.getenv('RATING')
PATH_DB = os.getenv('PATH_DB')
PATH_PRINT_GAME_OVER = os.getenv('PATH_PRINT_GAME_OVER')
PATH_PLAYERS = os.getenv('PATH_PLAYERS')
PATH_TEMP_NEW_USER = os.getenv('PATH_TEMP_NEW_USER')
