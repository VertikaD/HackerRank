# code by Vertika Dhingra.
import functools
arr = [
    [6, 6, 7, -10, 9, -3, 8, 9, -1],

    [9, 7, -10, 6, 4, 1, 6, 1, 1],

    [-1, -2, 4, -6, 1, -4, -6, 3, 9],

    [-8, 7, 6, -1, -6, -6, 6, -7, 2],

    [-10, -4, 9, 1, -7, 8, -5, 3, -5],

    [-8, -3, -4, 2, -3, 7, -5, 1, -5],

    [-2, -7, -4, 8, 3, -1, 8, 2, 3],

    [-3, 4, 6, -7, -7, -8, -3, 9, -6],

    [-2, 0, 5, 4, 4, 4, -3, 3, 0],
]


n = 9
# Primary Diagonal
primary_diag = []
for i in range(n):
    # adding values of left to right diagonal in a list.
    primary_diag.append(arr[i][i])
# Summation of elements of primary diagonal without using for loop.
# Used reduce function which apply lambda function to sum elements and returns final sum.
primary_diag_sum = functools.reduce(lambda a, b: a+b, primary_diag)

# Secondary Diagonal
# doing reverse range to reverse every row in square matrix.
secondary_diag = []
for i in range(n):
    for x in reversed(range(n)):
        secondary_diag.append(arr[i][x])


final_secondary_diag = []
# skipping 3 elements to get the diagonal elements.
for y in secondary_diag[::n+1]:
    final_secondary_diag.append(y)


# Summation of elements ofsecondary diagonal without using for loop.
final_secondary_diag_sum = functools.reduce(
    lambda a, b: a+b, final_secondary_diag)

# finally, calculating the difference of summation of diagonal elements in a sq. matrix.
Difference = abs(primary_diag_sum - final_secondary_diag_sum)
print(int(Difference))
