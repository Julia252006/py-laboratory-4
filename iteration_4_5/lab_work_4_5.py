# Create own enumerate function with count started from 1 bot from 0

print('\n\Laboratory Work 4.5')

foo = [1, 2, 3, 4, 5]


def my_enumerate(lst):
    for item in lst:
        yield lst.index(item) + 1, item


for item in my_enumerate(foo):
    print(item)


