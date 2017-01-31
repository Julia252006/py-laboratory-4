
# 1. Create variable with numbers list from 0 to 9
# 2. Create variable with numbers list from 0 to 9 and step 2
# 3. Create empty list
# 4. Create function that find intersection between two list variable
# 5. Call function


print('\n\Laboratory Work 4.2')

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