import re
# Complete the solve function below.
# code by Vertika Dhingra.


def solve(s):
    # finding indices of all spaces in the given string.
    space_index = []
    for i in re.finditer(' ', s):
        space_index.append(i.start())

    for z in range(len(space_index)):
        s = (s[0].upper() + s[1:space_index[z]+1] + s[space_index[z] +
                                                      1:space_index[z]+2].upper() + s[space_index[z]+2:])

    return s
