#code by Vertika Dhingra.
from itertools import permutations

S,k = input().split()
perm = list(permutations(S,int(k)))

perm_sort = sorted(perm)
for x in perm_sort:
    print(*x,sep='')