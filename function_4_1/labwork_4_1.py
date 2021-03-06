'''
'Task:
Refactor given program code:
1. Put reusable code into the functions:
   1.1. First - to calculate days in year
   1.2. Second – to decide which planet year is bigger
2. Put orbital_radius and orbital speed_together in same data structure
Optional: add try/except handlers to avoid entering incorrect planet
'''

import math
import sys

planet_data = {

    'orbital_radius': {"Mercury": 58,          # millions of kilometres
                       "Venus": 108,
                       "Earth": 150,
                       "Mars": 228,
                       "Jupiter": 778,
                       "Saturn": 1429,
                       "Uranus": 2871,
                       "Neptune": 4504
    },
     'orbital_speed': {"Mercury": 47.87,       #kilometres per second
                       "Venus": 35.02,
                       "Earth": 29.78,
                       "Mars": 24.13,
                       "Jupiter": 13.07,
                       "Saturn": 9.69,
                       "Uranus": 6.81,
                       "Neptune": 5.43
     }
}

import math
import sys


planet_data = {

    'orbital_radius': {"Mercury": 58,          # millions of kilometres
                       "Venus": 108,
                       "Earth": 150,
                       "Mars": 228,
                       "Jupiter": 778,
                       "Saturn": 1429,
                       "Uranus": 2871,
                       "Neptune": 4504
    },
     'orbital_speed': {"Mercury": 47.87,       #kilometres per second
                       "Venus": 35.02,
                       "Earth": 29.78,
                       "Mars": 24.13,
                       "Jupiter": 13.07,
                       "Saturn": 9.69,
                       "Uranus": 6.81,
                       "Neptune": 5.43
     }
}

planet1 = 'Earth'
planet2 = 'Venus'

orbital_radius = {"Mercury": 58, "Venus": 108, "Earth": 150, "Mars": 228, "Jupiter": 778, "Saturn": 1429,
                  "Uranus": 2871, "Neptune": 4504}  # millions of kilometres
orbital_speed = {"Mercury": 47.87, "Venus": 35.02, "Earth": 29.78, "Mars": 24.13, "Jupiter": 13.07, "Saturn": 9.69,
                 "Uranus": 6.81, "Neptune": 5.43}  # kilometres per second

planet1 = input("Planet 1: ")

orbital_radius_1 = orbital_radius[planet1] * 1000000  # turning millions of kilometres to kilometres
orbital_speed_1 = orbital_speed[planet1]

planet_year1 = 2 * math.pi * orbital_radius_1 / orbital_speed_1
planet_year1 = planet_year1 / (60 * 60 * 24)  # converting seconds to days

planet2 = input("Planet 2: ")
orbital_radius_2 = orbital_radius[planet2] * 1000000  # turning millions of kilometres to kilometres
orbital_speed_2 = orbital_speed[planet2]

planet_year2 = 2 * math.pi * orbital_radius_2 / orbital_speed_2
planet_year2 = planet_year2 / (60 * 60 * 24)  # converting seconds to days

print("The year is {} days on {}".format(int(planet_year1), planet1))
print("The year is {} days on {}".format(int(planet_year2), planet2))

bigger_year = planet1 if planet_year1 > planet_year2 else planet2  # Looking which year is bigger

print("The {} year is bigger".format(bigger_year))

