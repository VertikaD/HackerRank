# code by Vertika Dhingra.
# 10/17 test cases passed.
from itertools import chain, combinations
import itertools

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    if k==1:
        return 1
    elif k==2:
        return 2
    else:
        # finding all the possible subsets of set(s).
        subsets_x = list(combinations(s, 2))
        # print(subsets_x)
        subsets_y = list(chain.from_iterable(combinations(s, r)
                                             for r in range(3, len(s)+1)))
        # print(subsets_y)

        subset_1 = []
        for i in subsets_x:
            if (sum(list(i)) % k != 0):
                subset_1.append(i)

        # sum of elements pair wise in all subsets and checking the divisibility.
        list_NonDivisibleSubset = []
        sum_s = []
        for y in subsets_y:
            sum_1 = []
            for i, x in itertools.combinations(y, 2):
                sum_1.append((i+x))
            sum_s.append(sum_1)
        # print(sum_s)

        indices_ND = []
        for e, l in enumerate(sum_s):
            # gives false as one of them is divisible by 3.
            Result = all(a % k != 0 for a in l)
            if Result == True:
                # got the index whose all sum is not divisible by the given non factor.
                indices_ND.append(e)

        # print(indices_ND)

        # match these indices with subsets_y
        subset_2 = []
        for i in indices_ND:
            for y in range(len(subsets_y)):
                if i == y:  # if indices match , append the matched list in new list.
                    subset_2.append(subsets_y[y])

        Minimal_subsets = subset_1+subset_2
        Size_Maximal_Subset = max(map(len, Minimal_subsets))
        return Size_Maximal_Subset
