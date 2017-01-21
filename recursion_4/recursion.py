# 1. Print number in range in both directoin
# 2. Calculate factorial of input number / data
# 3. Calculate arithmetical mean of input number / data structure number
# 4. Harmonic mean of N: N / (1/1 +1/2 .... 1/N)
# 5.Calculate sum of even numbers and multiplicity of odd numbers
# of input number / data structure
#
#


#1. Print number in range in both directoin printing

def num_walking(n, order=True, c=0):
    if order:
        print(n)
        return num_walking(n - 1, order) if n > 0 else 0
    else:
        print(c)
        return num_walking(n, order, c + 1) if c < n else n

# num_walking(5)
# num_walking(5,  False)


# 3. Calculate arithmetical mean of input number / data structure
# number
def average_mean(n):
    def sum(c=1):
        return c + sum(c + 1) if c < n else c
    return sum() / n

# print(average_mean(5))

# 4. Harmonic mean of N: N / (1/1 +1/2 .... 1/N)
def harmonic_mean(n):
        def sum(c=1):
            return 1 / c + sum(c + 1) if c < n else 1 / c
        return n / sum()

# print (harmonic_mean(3))

# 5.Calculate sum of even numbers and multiplicity of odd numbers
# of input number / data structure
def nums_operations(n, evens=0, odds=1):
    evens += n if n % 2 == 0 else 0
    odds *= n if n % 2 != 0 else 1
    return nums_operations(n - 1, evens, odds) if n > 0 else 'evens sum: {}\n'\
                                                             'odds multi: {}'\
                                                            .format(evens, odds)
#print(nums_operations(5))

def avarage_mean(li):
    def elems_sum(i=0, sum=0):
        sum += li[i]
        return elems_sum(i + 1, sum) if i < len(li) - 1 else sum
    return elems_sum() / len(li)

#print('avarage mean of {} is {}'.format([1, 2, 3, 4], avarage_mean([1, 2, 3, 4])))


def harmonic_mean(li):
    def elems_sum(i=0, sum=0):
        sum += 1 / li[i]
        return elems_sum(i + 1, sum) if i < len(li) - 1 else sum
    return len(li) / elems_sum()

#print('harmonic mean of {} is {}'.format([1, 2, 3, 4], harmonic_mean([1, 2, 3])))

