from math import pi

# closure - nested function,
# that has access to arguments passed to its enclosed function


# closure allows to decrease number of arguments for target algorithm
def hello(name):
    print('Hello, ', name, '!')


def closure_hello(name):
    def print_hello(): # print hello function does not has additional parameters of name
        print('Hello, ', name, '!')
        print_hello()


# hello('Julia')
# closure_hello('Julia')

# Closure task #1
#    Create function, that calculates circule area (parameters: radius or diameter)
#    with closure of get_radius_square(), get_pi()


def get_circle_area(radius, diameter=5):
    def get_pi():
        return pi

    def get_radius_square():
        return radius * radius if not radius == None else (diameter / 2) * (diameter / 2)
    return get_pi() * get_radius_square()


print(get_circle_area(2))  # radius 2
print(get_circle_area(None, diameter=3))  # assign new value to diameter parameter
print(get_circle_area(None))  # using of default radius parameter


# Closure task #2
#   The same as task #1, but find length of the circule
def get_circle_length(radius, diameter=5):
    def get_pi():
        return pi

    def get_diameter():
        return radius * 2 if not radius == None else diameter
    return get_pi() * get_diameter()

print(get_circle_length(2))  # radius 2
print(get_circle_length(None, diameter=3))  # assign new value to diameter parameter
print(get_circle_length(None))  # using of default radius parameter



# Closure task #3
#  Create function separate_evens_and_odds, that return two sub-lists of
#  whole list passed to the function as parameter.
#  separate_event_and_odds must have next closures:
#  is_even_predicate(), det_evens(), det_odds()
#  Optional: use generators while implementing closures above






