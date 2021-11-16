import os
import datetime
import re
import random

from config import PATH_PLAYERS, PATH_TEMP_NEW_USER, RATING, PATH_TEMP_START_STATUS, LIVES, PATH_PRINT_GAME_OVER
# LIVES, RATING, PATH_DB, PATH_PRINT_GAME_OVER,


def creating_record_database(rating: int, time: str) -> str:
    with open(file=PATH_TEMP_NEW_USER, encoding='utf-8') as file:
        data = file.read()
        data = data.format(RATING=rating, TIME=time)
        return data


def game_over():
    with open(file=PATH_PRINT_GAME_OVER, mode='r', encoding='utf-8') as file:
        _game_over = file.read()
        print('----------', _game_over, sep='\n')


def status(user_data: dict):
    with open(file=PATH_TEMP_START_STATUS, mode='r', encoding='utf-8') as file:
        _status = file.read()
        _status = _status.format(name=user_data['name'],
                                 rating=user_data['rating'], time=user_data['time'], lives=user_data['lives'])
        print('----------', _status, sep='\n')


def parser_data_user(name: str) -> tuple:
    user_path = r"{path}\{user_name}".format(path=PATH_PLAYERS, user_name=name)
    with open(file=user_path, encoding='utf-8') as file:
        user_data = file.read()
    re_match = re.match(pattern=r'RATING:(?P<rating>\d+)\nTIME:(?P<time>.+)', string=user_data)
    rating = int(re_match.group('rating'))
    time = re_match.group('time')
    return rating, time, user_path


def new_user(name: str) -> tuple:
    user_path = r"{path}\{user_name}".format(path=PATH_PLAYERS, user_name=name)
    time_now = datetime.datetime.now()
    _new_user = creating_record_database(rating=RATING, time=time_now)
    print('----------', _new_user, sep='\n')
    with open(file=user_path, mode='a', encoding='utf-8') as new_user_file:
        new_user_file.write(_new_user)
    return int(RATING), time_now, user_path


def task_creation() -> tuple:
    a = random.randint(a=0, b=10)
    b = random.randint(a=0, b=10)
    true_c = a + b
    return a, b, true_c


def start() -> dict:
    name = input('name:')
    list_users = os.listdir(path=PATH_PLAYERS)
    if name in list_users:
        rating, time, user_path = parser_data_user(name=name)
    else:
        rating, time, user_path = new_user(name=name)
    return dict(name=name, rating=rating, lives=int(LIVES), time=time, user_path=user_path)


def exit(user_data: dict):
    print_exit = r'The user {name} quits the game. Your {rating} rating is saved.'.format(
        rating=user_data['rating'], name=user_data['name'])
    with open(file=user_data['user_path'], mode='w', encoding='utf-8') as file:
        user_data = creating_record_database(rating=user_data['rating'], time=user_data['time'])
        file.write(user_data)
    print('----------', print_exit, sep='\n')


def rating_function(lives, a, b):
    return 1


def answer_isdigit(a: int, b: int, true_c: int, user_c: int, user_data: dict) -> tuple:
    user_c = int(user_c)
    if true_c == user_c:
        user_data['rating'] += rating_function(lives=user_data['lives'], a=a, b=b)
        return False, user_data
    else:
        user_data['lives'] -= 1
        if user_data['lives'] == 0:
            user_data['rating'] = 0
            game_over()
            user_data['lives'] = LIVES
            return False, user_data


def answer_is_not_digit(attempt: int, user_data: dict) -> tuple:
    if attempt == 0:
        if user_data['lives'] == 0:
            print('----------',
                  "You're out of life. lives:{}".format(user_data['lives']), sep='\n')
            game_over()
            user_data['rating'] = 0
            user_data['lives'] = LIVES
            return False
        else:
            user_data['lives'] -= 1
            print('----------',
                  'Enter the number, you lose lives. lives:{}'.format(user_data['lives']), sep='\n')
    else:
        print('----------',
              'please enter the number. attempt:{attempt}'.format(attempt=attempt), sep='\n')
        attempt -= 1


def task_solution(user_data: dict) -> dict:
    a, b, true_c = task_creation()
    attempt = 3
    game_status = True
    while game_status:
        user_c = input('{a} + {b} = '.format(a=a, b=b))
        if user_c.isdigit():
            game_status, user_data = answer_isdigit(true_c=true_c,
                                                    user_c=user_c,
                                                    user_data=user_data,
                                                    a=a,
                                                    b=b)
        else:
            attempt, user_data = answer_is_not_digit(attempt=attempt, user_data=user_data)  
    return user_data


def main():
    user_data = start()
    while True:
        status(user_data=user_data)
        print('----------', '1. next\n2. exit\n(write 1 or 2)', sep='\n')
        answer = input('enter answer: ')
        if answer == '2':
            exit(user_data=user_data)
            break
        elif answer == '1':
            user_data = task_solution(user_data=user_data)


if __name__ == "__main__":
    main()
