# Complete the cutTheSticks function below.
# code by Vertika Dhingra.
def cutTheSticks(arr):
    sticks_cut = []
    while len(arr) != 0:  # loop will continue till list is empty.
        # calculating length of shortest stick remaining after every iteration.
        minimum = min(arr)
        # subtracting the min element from all elements.
        # cutting the sticks into smaller sticks.
        arr[:] = [i-minimum for i in arr]
        # number of sticks that are left before each iteration until none left.
        sticks_cut.append(len(arr[:]))

        for i in arr[:]:
            if i == 0:
                arr.remove(i)

    # Returning number of sticks after every iteration.
    return sticks_cut
