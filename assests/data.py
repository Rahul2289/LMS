from config import DEPTS, YEARS, SEMS
from libs import json
import os

# Get the base directory of the project dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the LMS.json file relative to this file
LMS_PATH = os.path.join(BASE_DIR, "LMS.json")

LOGIN_NAME = ''

# Load data
with open(LMS_PATH, 'r') as f:
    LMS = json.load(f)

# Save data
def save_data():
    with open(LMS_PATH, 'w') as f:
        json.dump(LMS, f, indent=4)
        
# with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'r') as f:
#     LMS = json.load(f)

# def save_data():
#     with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'w') as f:
#         json.dump(LMS, f, indent=4)