Brain Academy. Python Course. Laboratory Work #4

Laboratory Work #4.1.

Task:
Refactor given program code:
1. Put reusable code into the functions:
   1.1. First - to calculate days in year
   1.2. Second – to decide which planet year is bigger
2. Put orbital_radius and orbital speed_together in same data structure
Optional: add try/except handlers to avoid entering incorrect planet
    
 Here is its solution code: 
    
```python 
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

```

Laboratory Work #4.2.
Task:
 1. Create variable with numbers list from 0 to 9
 2. Create variable with numbers list from 0 to 9 and step 2
 3. Create empty list
 4. Create function that find intersection between two list variable
 5. Call function
  Here is its solution code: 
    
```python 
var1 = list(range(10))
var2 = list(range(0,10,2))
res = []

def intersect(var1, var2):
    res = []
    for x in var1:                # Scan seq1
        if x in var2:             # Common item?
            res.append(x)         # Add to end
    return res

print(intersect(var1, var2))
print("List:", res)
```

Laboratory Work #4.3.
Task:
 1. Create string variable word
 2. Create dictionary variable ids
 3.  Create function_4_1 that include at least 2 arguments_4_3 word and name from ids dictionary
 4. Function also should have one default argument age
 5. If additional arguments will added to function call it should work properly
 6. During first function calling use unpack arguments from dictionary ids
 7. During second call use ids key value and some range of values
 
 ```python 
 word = 'Found name:'
ids = {'name':"Alice", 'age':27}

def intersection(word,name,*args,age=None):
    print(word, name)
    print('Age:',age)
    print(args)

intersection(word, **ids)
intersection(word, ids['name'], *list(range(10)))
 ```
 
Laboratory Work #4.4.
Task:
1. Refactor given program code:
   foo = [1, 2, 3, 4, 5]
   odd_foo = []
   def isOdd(x):
     return x % 2 == 1
   for f in foo:
     if isOdd(f):
        odd_foo.append(f)
   print (odd_foo)
3. Use list comprehension for this task
4.  Use filter with lambda function for this task
5. Solutions should have only one line of code

```python 
 foo = [1, 2, 3, 4, 5]
odd_foo = []

def isOdd(x):
    return x % 2 == 1
for f in foo:
    if isOdd(f):
        odd_foo.append(f)
print (odd_foo)


odd_foo = [x for x in foo if x % 2 == 1]

odd_foo = filter(lambda x: x % 2 == 1, foo)
```
  
  Laboratory Work #4.5.
Task:
Create own enumerate function with count started from 1 bot from 0

```python 
 print('\n\Laboratory Work 4.5')

foo = [1, 2, 3, 4, 5]


def my_enumerate(lst):
    for item in lst:
        yield lst.index(item) + 1, item


for item in my_enumerate(foo):
    print(item)
```

Laboratory Work #4.6.
Task:
Create function that write some info 
 into file object and flash data in decorator part
 
```python 
 
 
```