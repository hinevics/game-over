import os
import datetime
# import re
# import random

from config import PATH_PLAYERS, PATH_TEMP_NEW_USER, RATING
# LIVES, RATING, PATH_DB, PATH_PRINT_GAME_OVER,


def parser_data_user(user):
    # a = re.
    pass


def start():
    name = input('name:')
    list_users = os.listdir(path=PATH_PLAYERS)
    if name in list_users:
        parser_data_user()
    else:
        PATH_NEW_USER = r"{path}\{user_name}".format(path=PATH_PLAYERS, user_name=name)
        with open(file=PATH_NEW_USER, mode='a', encoding='utf-8') as new_user_file:
            time_now = datetime.datetime.now()
            new_user = PATH_TEMP_NEW_USER.format(RATING=RATING, TIME=time_now)
            new_user_file.write(new_user)


def main():
    start()


if __name__ == "__main__":
    main()
