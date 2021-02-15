# Enter your code here. Read input from STDIN. Print output to STDOUT
# code by Vertika Dhingra.
N, M = map(int, input().split())
n = int(N/2)
# N = no of rows.
# M = width/no of columns.

# printing the first half of door mat.
for i in range(n):
    c = '.|.' * ((2*i)+1)
    print(c.center(M, '-'))

# Center part of the mat.
print('WELCOME'.center(M, '-'))

# printing the second half of door mat.
# reversed function reverses the range thus reversing the triangle.
for i in reversed(range(n)):
    c = '.|.' * ((2*i)+1)
    print(c.center(M, '-'))
