# Enter your code here. Read input from STDIN. Print output to STDOUT
# Nested Logic
# Implementation of datetime objects in python.
# code by Vertika Dhingra
from datetime import datetime
from datetime import date

d1, m1, y1 = [int(x) for x in input().split()]
returned_date = date(y1, m1, d1)

d2, m2, y2 = [int(x) for x in input().split()]
due_date = date(y2, m2, d2)

if (returned_date == due_date) or (returned_date < due_date):
    fine = 0
    print(fine)
if ((returned_date.day) > (due_date.day)) and (returned_date.month == due_date.month) and (returned_date.year == due_date.year):
    fine = (15 * (returned_date.day - due_date.day))
    print(fine)
if ((returned_date.month) > (due_date.month)) and (returned_date.year == due_date.year):
    fine = (500 * (returned_date.month-due_date.month))
    print(fine)
if (returned_date.year > due_date.year):
    fine = 10000
    print(fine)
