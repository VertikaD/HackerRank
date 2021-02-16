#code by Vertika Dhingra.

matrix = [
    [1, 2, 3, 4, 5, 6],
    [9, 8, 7, 6, 5, 4],
    [3, 4, 5, 4, 5, 6],
    [9, 8, 7, 6, 5, 4],
    [1, 2, 3, 4, 5, 6],
    [9, 8, 7, 6, 5, 4],
]

# this function is optimises the code.


def all_hour_glasses(p, q):
    # this function calculates sum of all 16 hourglasses.
    def hour_glass(n, m):
        # nested List Comprehension.
        hour_glass_list = [matrix[i][n:m]
                           for row in matrix[:1] for i in range(p, q)]

        # making a proper hourglass . # this remains same for every hourglass.
        del hour_glass_list[1][0]
        del hour_glass_list[1][1]

        # now,we will flatten this nested list to calculate the sum using list comprehension.
        hour_glass_list_f = [
            val for innerlist in hour_glass_list for val in innerlist]

        # Finally, calculating sum of elements in Hour Glass.
        sum = 0
        for i in hour_glass_list_f:
            sum += i

        return(sum)

    sum_list = [hour_glass(i, i+3) for i in range(4)]
    return sum_list


sum_Four = [all_hour_glasses(d, d+3) for d in range(4)]
sum_Four_list = [val for innerlist in sum_Four for val in innerlist]
# calculating the maximum sum from all the 16 hour glasses.
print(max(sum_Four_list))
