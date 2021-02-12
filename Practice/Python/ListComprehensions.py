# ListComprehensions
from itertools import product
if __name__ == '__main__':  # code by Vertika Dhingra
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# calculating all permutations of all coordinates: (i, j, k) or (x, y, z).
# We have used product from itertools to compute lexicographic increasing order of permutations.
perm = list(product(range(x+1), range(y+1), range(z+1)))
print(perm)

# converting list of tuples into list of lists.
all_permutations = [list(i) for i in perm]

# Printing a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k)is not equal to n.
# USING LIST COMPREHENSION INSTEAD OF NESTED FOR LOOP.
print([i for i in all_permutations if sum(i) != n])


# # BELOW IN COMMENTS , WE HAVE THE EQUIVALENT NESTED FOR LOOPS for the above LIST COMPREHENSION.
# # sum = 0
# # Result = []
# # for i in all_permutations:
# #     for x in range(len(i)):
# #         sum = sum + i[x]
# #     if sum != n:
# #         Result.append(i)
