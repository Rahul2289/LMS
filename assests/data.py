from config import DEPTS, YEARS, SEMS
from libs import json

with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'r') as f:
    LMS = json.load(f)

def save_data():
    with open('C:/Users/Rahul/innomatics-448/LMS/assests/LMS.json', 'w') as f:
        json.dump(LMS, f, indent=4)

# LMS = {}
# LMS['ADMINS'] = [{"name": "Rahul", "password": "Rahul@123"},{"name": "Akhil", "password": "Akhil@123"}]


# def initialize_data():
#     LMS['STUDENTS'] = {}
#     LMS['TEACHERS'] = {}
#     LMS['BOOKS'] = {}

#     for dept in DEPTS:
#         LMS['STUDENTS'][dept] = {}
#         for year in YEARS:
#             LMS['STUDENTS'][dept][year] = {}
#             for sem in SEMS:
#                 LMS['STUDENTS'][dept][year][sem] = []
    
#     for dept in DEPTS:
#         LMS['TEACHERS'][dept] = {}
#         for year in YEARS:
#             LMS['TEACHERS'][dept][year] = {}
#             for sem in SEMS:
#                 LMS['TEACHERS'][dept][year][sem] = []
    
#     for dept in DEPTS:
#         LMS['BOOKS'][dept] = {}
#         for year in YEARS:
#             LMS['BOOKS'][dept][year] = {}
#             for sem in SEMS:
#                 LMS['BOOKS'][dept][year][sem] = []

#     LMS['STUDENTS']["CSE"]["1-YEAR"]["1-SEM"].append({"name": "rahul", "password": "rahul"})
#     LMS['TEACHERS']["CSE"]["1-YEAR"]["1-SEM"].append({"name": "akhil", "password": "akhil"})
#     LMS['BOOKS']["CSE"]["1-YEAR"]["1-SEM"].append({"name": "python", "author": "rahul", "quantity": 1})