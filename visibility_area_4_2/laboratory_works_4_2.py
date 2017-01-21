
# 1. Create variable with numbers list from 0 to 9
# 2. Create variable with numbers list from 0 to 9 and step 2
# 3. Create empty list
# 4. Create function that find intersection between two list variable
# 5. Call function


print('\n\Laboratory Work 4.2')

seq1 = list(range(10))
seq2 = list(range(0,10,2))
res = []
def intersection(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

print(intersection(seq1, seq2))
print("List:", res)