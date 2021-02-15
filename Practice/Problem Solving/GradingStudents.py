import math


def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for i in range(len(grades)):
        if grades[i] < 38:
            final_grades.append(grades[i])
        else:
            # finding next multiple of 5 from N.
            next_multiple = (math.ceil(grades[i]/5)*5)
            if (next_multiple-grades[i] < 3):
                final_grades.append(next_multiple)
            else:
                final_grades.append(grades[i])

    return final_grades
