#SECOND LOWEST IN LIST
if __name__ == '__main__':  # code by Vertika Dhingra
    list_name = []
    list_score = []
    for _ in range(int(input())):
        name = input()
        list_name.append(name)  # storing name inputs into a list.
        Score = float(input())
        list_score.append(Score)  # storing score inputs into a list.

# combining the two lists into a single list of tuples.
student_record = list(zip(list_name, list_score))

student_record_list = []  # creating an empty list

[student_record_list.append(list(i))
 for i in student_record]  # converting list of tuples
# into list of lists or nested list using List Comprehension.

# Sorting the list on the basis of grades or scores.
student_record_list.sort(key=lambda score: score[1])

# APPROACH :
# FOR HANDLING REPITITION ISSUES , MY APPROACH IS TO
# 1) FETCH THE SCORES ,
# 2)CALCULATE THE FREQUENCY OF SCORES USING DICT.
# 3)STORING THE FREQUENCY OF THE LEAST SCORE AND THEN SECOND LEAST SCORE.
# 4) ITERATING OVER THE SORTED NESTED LIST TILL THE FREQUENCY.
# OF LEAST SCORE AND THEN SECOND LEAST SCORE AND PRINTING NAMES OF THE STUDENT.


# list comprehension of nested lists
num = [inner[1] for inner in student_record_list]
num.sort()  # sorting in ascending order. #here , sorting is already done .

score_frequency = {}  # empty dictionary to calculate frequency.
for i in num:
    if i in score_frequency:
        score_frequency[i] += 1
    else:
        score_frequency[i] = 1

score_frequency_tuple = score_frequency.items()  # convert dict into tuple
s = list(score_frequency_tuple)

score_frequency_list = []
[score_frequency_list.append(list(i))
 for i in s]  # convert tuple into nested list

# now since I have the list of scores with its frequencies in a list , I can fetch
# the smallest score and later second smallest score with its frequency.

least_score = score_frequency_list[0][0]
least_score_frequency = int(score_frequency_list[0][1])


# printing names of the students having lowest grade.
names_lowest_grade = [i[0]
                      for i in student_record_list[:least_score_frequency]]

# TASK 2 : PRINT THE NAMES WHICH HAVE THE SECOND LOWEST GRADE.

second_least_score = score_frequency_list[1][0]
second_least_score_frequency = int(score_frequency_list[1][1])


# printing names of the students having second lowest grade.
names_second_lowest_grade = [
    i[0] for i in student_record_list[least_score_frequency:least_score_frequency+second_least_score_frequency]]
names_second_lowest_grade.sort()  # sorting names alphabetically.
print(names_second_lowest_grade)

for N in names_second_lowest_grade:
    print(N)
