from gui import *
import functions as func

DEFAULT_BG_COLOR = "#626366"

users = {
    "admin": "admin",
    "alexandre": "123"
}

habits_list = ['wake up early', 'read 10 pages', 'exercise', 'drink 5L of water']

# func.write_json_users(users)
# func.read_json_users()

create_window(DEFAULT_BG_COLOR, habits_list)
