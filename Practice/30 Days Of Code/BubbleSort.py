# Bubble Sort
n = [4, 3, 2, 1]

# This outer loop is used to continue traversing till no of swaps is zero.
# Also,it tracks number of elements swapped during a single traversal.
for i in range(len(n)):
    # calculating the number of swaps for each traversal.
    count = 0
    # iterating len(n)-1 times because number of comparisons will be len(n)-1 times.
    for x in range(len(n)-1):
        # if value at first index is greater than value at second index.
        if n[x] > n[x+1]:
            n[x], n[x+1] = n[x+1], n[x]  # Swap.
            count += 1  # Incrementing the count by 1 if numbers got swapped.

    if count == 0:  # if no elements were swapped during a traversal , list is sorted.
        break  # coming out of the outer loop.
