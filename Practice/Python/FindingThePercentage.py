if __name__ == '__main__':  # Code by Vertika Dhingra.
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# getting the values of the key.
query_name_marks = student_marks.get(query_name)
# print(query_name_marks)
Average = sum(query_name_marks)/len(query_name_marks)
print('{0:.2f}'.format(Average))
