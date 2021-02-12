# code by Vertika Dhingra.
import math

AB = int(input())
BC = int(input())

result = math.atan2(AB, BC)  # returns the arc tangent.
degree_sign = u"\N{DEGREE SIGN}"  # to print the degree symbol.
print(round(math.degrees(result)), degree_sign, sep='')

# MY INSIGHTS ON THIS PROBLEM.
# Below , is my previous implementations :
# we could use asin but asin cannot accept range more than 1.
# Also , asin was only passing two test cases (10,10) and (56,54).
# so to tackle this problem , we can use atan2() which takes
# two parameters(length of sides) and returns the arc tangent.
# AC = math.sqrt((AB**2)+(BC**2))
# C_p = abs(AC)
# MC = C_p/2
# sinQ = MC/BC
# print(round(math.degrees(math.asin(sinQ))))
