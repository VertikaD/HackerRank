#code by Vertika Dhingra.
from itertools import product

A= map(int,input().split())
B= map(int,input().split())

cartesian_product= list(product(A,B))
print(*cartesian_product)