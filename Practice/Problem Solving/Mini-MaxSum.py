from itertools import permutations

# Complete the miniMaxSum function below.

# code by Vertika Dhingra.


def miniMaxSum(arr):
    # If all numbers in a list is same .
    if len(set(arr)) == 1:
        # printing the min , max sum of same elements.
        print(sum(arr[:4]), sum(arr[:4]))

    else:

        arr_p = permutations((arr), 4)
        all_pairs = [i for i in list(arr_p)]

        # Finding unique pairs from permutations irrespective of the order.
        # Using sets , as sets only accept unique values.
        unique_set = set(tuple(frozenset(x)) for x in set(all_pairs))
        unique = list(unique_set)

        # Now , finding sum of all unique pairs of 3 .
        sum_all = []
        [sum_all.append(sum(i)) for i in unique]
        # Printing two spaced integers denoting respective minimum and maximum values.
        print(min(sum_all), max(sum_all))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
