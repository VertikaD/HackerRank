import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
# code by Vertika Dhingra.
def compareTriplets(a, b):
    Result = []
    a_score = 0
    b_score = 0
    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
        else:
            pass

    Result.append(a_score)
    Result.append(b_score)
    return Result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
