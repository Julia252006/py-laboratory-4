# Curring  - is a function programing tool, that mean
# using several functions with one argument instead of one function
# with several arguments

def move_forward_point(x, y, z, vector):
    return (x + vector, y + vector, z + vector)

# after curring
def get_vector():
    return 5

def move_forward_x_axis(x):
    return x + get_vector()

def move_forward_y_axis(y):
    return y + get_vector()

def move_forward_z_axis(z):
    return z + get_vector()


# Curring task # 1
#   Given function resize_rectangle(), which takes tree parameters^
#       width, height, step
#   Modify its implementation, using curring


def resize_rectangle(width, height, step):
    return [width + step, height + step]


# Answer: after curring

def get_side(side_name):
    side = 0
    try:
        side = int(input('Please, enter the resize step for' + side_name + ':'))
    except ValueError:
        print('ValueError accured!')
    return side


def get_step(side_name):
    step = None
    try:
        step = int(input('Please, enter the resize step for' + side_name + ':'))
    except ValueError:
        print('ValueError accured!')
    return step


def get_width(width):
    return width + get_step('width')


def get_height(height):
    return height + get_step('height')


def get_new_rectangle_size():
    return [get_width(get_side('width')), get_height(get_side('height'))]


print(get_new_rectangle_size())
