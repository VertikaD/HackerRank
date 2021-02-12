# SECOND MAXIMUM IN A LIST.
if __name__ == '__main__':  # code by Vertika Dhingra
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort(reverse=True)  # sorting list in descending order.

# handling the repetition issue .
# empty dictionary to calculate frequency of each element in list.
arr_frequency = {}
for i in arr:
    if i in arr_frequency:
        arr_frequency[i] += 1
    else:
        arr_frequency[i] = 1

arr_frequency_tuple = arr_frequency.items()  # convert dict into tuple
s = list(arr_frequency_tuple)

arr_frequency_list = []
[arr_frequency_list.append(list(i))
 for i in s]  # convert tuple into nested list

# now since I have the list of scores with its frequencies in a list , I can fetch
# the maximum score and later second maximum score with its frequency.

max_score = arr_frequency_list[0][0]  # max score
max_score_frequency = int(arr_frequency_list[0][1])  # max score frequency


second_max_score = arr_frequency_list[1][0]  # second max score
# second max score frequency.
second_max_score_frequency = int(arr_frequency_list[1][1])

# Now, since arr is already sorted in descending order .
# we will iterate in the arr list till the end of max score till we reach second max score.

Runner_Up_Score = [
    x for x in arr[max_score_frequency:max_score_frequency+second_max_score_frequency]]
print(Runner_Up_Score[0])
