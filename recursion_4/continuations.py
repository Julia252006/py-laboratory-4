# Continuations- a functional programing tool, that replace each function
# to its reference, making code more concies and readable

import math

# hypotenuse = math.sqrt(
 #   (math.pow(int(input('cathetus a: ')), 2)) +
  #  (math.pow(int(input('cathetus a: ')), 2))
#)

# print(hypotenuse)

# after continuation:

def get_side(cathetus_name=''):
    side = 1
    try:
        side = int(input('cathetus {}: '.format(cathetus_name)))
    except:
        print()
    return side

side_a = get_side('a')
side_b = get_side('b')
side_square_a = math.pow(side_a, 2)
side_square_b = math.pow(side_b, 2)
hypotenuse_square = side_square_a + side_square_b
hypotenuse = math.sqrt(hypotenuse_square)

print(hypotenuse)
