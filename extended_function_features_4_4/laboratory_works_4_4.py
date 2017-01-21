# Refactor given program code:
# foo = [1, 2, 3, 4, 5]
#  odd_foo = []
# def isOdd(x):
# return x % 2 == 1
# for f in foo:
# if isOdd(f):
# odd_foo.append(f)
# print (odd_foo)
# Use list comprehension for this task
# Use filter with lambda function for this task
# Solutions should have only one line of code

print('\n\Laboratory Work 4.4')

foo = [1, 2, 3, 4, 5]
odd_foo = [x for x in foo if x % 2 == 1]
odd_foo = filter(lambda x: x % 2 == 1, foo)










