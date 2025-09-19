from config import DEPTS, YEARS, SEMS

LMS = {}
LMS['ADMINS'] = [{"name": "Rahul", "password": "Rahul@123"},{"name": "Akhil", "password": "Akhil@123"}]

def initialize_data():
    LMS['STUDENTS'] = {}
    LMS['TEACHERS'] = {}
    LMS['BOOKS'] = {}

    for dept in DEPTS:
        LMS['STUDENTS'][dept] = {}
        for year in YEARS:
            LMS['STUDENTS'][dept][year] = {}
            for sem in SEMS:
                LMS['STUDENTS'][dept][year][sem] = []
    
    for dept in DEPTS:
        LMS['TEACHERS'][dept] = {}
        for year in YEARS:
            LMS['TEACHERS'][dept][year] = {}
            for sem in SEMS:
                LMS['TEACHERS'][dept][year][sem] = []