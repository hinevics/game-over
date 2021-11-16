import os
import datetime
# import re
# import random

from config import PATH_PLAYERS, PATH_TEMP_NEW_USER, RATING, PATH_TEMP_START_STATUS, LIVES, PATH_PRINT_GAME_OVER
# LIVES, RATING, PATH_DB, PATH_PRINT_GAME_OVER,


def game_over():
    with open(file=PATH_PRINT_GAME_OVER, mode='r', encoding='utf-8') as file:
        _game_over = file.read()
        print(_game_over)


def status(name: str, rating: str, time: str, lives: str):
    with open(file=PATH_TEMP_START_STATUS, mode='r', encoding='utf-8') as file:
        _status = file.read(name=name, rating=rating, time=time, lives=lives)
        print(_status)


def parser_data_user(user):
    # a = re.
    pass


def new_user(name: str) -> tuple:
    PATH_NEW_USER = r"{path}\{user_name}".format(path=PATH_PLAYERS, user_name=name)
    time_now = datetime.datetime.now()
    with open(file=PATH_TEMP_NEW_USER, mode='r', encoding='utf-8') as file:
        new_user = file.read()
        new_user = new_user.format(RATING=RATING, TIME=time_now)
        print(new_user)
    with open(file=PATH_NEW_USER, mode='a', encoding='utf-8') as new_user_file:
        new_user_file.write(new_user)
    return RATING, time_now


def task_creation():
    pass


def start():
    name = input('name:')
    list_users = os.listdir(path=PATH_PLAYERS)
    if name in list_users:
        rating, time = parser_data_user()
    else:
        rating, time = new_user(name=name)
    status(name=name, rating=rating, time=time, lives=LIVES)


def main():
    start()
    task_creation()


if __name__ == "__main__":
    main()
