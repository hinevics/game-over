import os
import datetime
# import re
# import random

from config import PATH_PLAYERS, PATH_TEMP_NEW_USER, RATING, PATH_TEMP_START_STATUS
# LIVES, RATING, PATH_DB, PATH_PRINT_GAME_OVER,


def parser_data_user(user):
    # a = re.
    pass


def new_user(name: str) -> tuple:
    PATH_NEW_USER = r"{path}\{user_name}".format(path=PATH_PLAYERS, user_name=name)
    with open(file=PATH_NEW_USER, mode='a', encoding='utf-8') as new_user_file:
        time_now = datetime.datetime.now()
        new_user = PATH_TEMP_NEW_USER.format(RATING=RATING, TIME=time_now)
        new_user_file.write(new_user)
    return RATING, time_now


def start():
    name = input('name:')
    list_users = os.listdir(path=PATH_PLAYERS)
    if name in list_users:
        rating, time = parser_data_user()
    else:
        rating, time = new_user(name=name)
    print_status = PATH_TEMP_START_STATUS.format()
    print(PATH_TEMP_START_STATUS)


def main():
    start()


if __name__ == "__main__":
    main()
