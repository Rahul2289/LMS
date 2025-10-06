from config import DEPTS, YEARS, SEMS
from libs import json

LOGIN_NAME = ''

with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'r') as f:
    LMS = json.load(f)

def save_data():
    with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'w') as f:
        json.dump(LMS, f, indent=4)
