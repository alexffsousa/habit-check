import json
from datetime import date



def get_day():
    today = date.today()
    today_date = today.strftime('%d %B')
    clock = today.strftime('%c')
    print(clock)
    return today_date, clock


def read_json_users():
    with open('users.json', 'r') as openfile:
        users_list = json.load(openfile)
    print(users_list)


def write_json_users(users_list):
    json_object = json.dumps(users_list, indent=4)
    with open('users.json', 'w') as users_file:
        users_file.write(json_object)


def read_habits():
    with open('habits.json', 'r') as openfile:
        habits_list = json.load(openfile)
    print(habits_list)


def write_habits(habits_list):
    json_object = json.dumps(habits_list, indent=4)
    with open('users.json', 'w') as habits_file:
        habits_file.write(json_object)
