import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
# This outer loop is used to continue traversing till no of swaps is zero.
# Also,it tracks number of elements swapped during a single traversal.
sum = 0
for i in range(n):
    # calculating the number of swaps for each traversal.
    count = 0
    # iterating len(n)-1 times because number of comparisons will be len(n)-1 times.
    for x in range(n-1):
        # if value at first index is greater than value at second index.
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]  # Swap.
            count += 1  # Incrementing the count by 1 if numbers got swapped.
            sum += 1
    if count == 0:  # if no elements were swapped during a traversal , list is sorted.
        break  # coming out of the outer loop.

print('Array is sorted in', sum, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
