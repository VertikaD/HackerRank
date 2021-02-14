# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for i in arr:
        if i > 0:
            count_pos += 1
        if i < 0:
            count_neg += 1
        if i == 0:
            count_zero += 1

    print('{:.6f}'.format(count_pos/n))
    print('{:.6f}'.format(count_neg/n))
    print('{:.6f}'.format(count_zero/n))
