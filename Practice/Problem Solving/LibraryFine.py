from datetime import datetime
from datetime import date

# Complete the libraryFine function below.
# code by Vertika Dhingra.


def libraryFine(d1, m1, y1, d2, m2, y2):
    returned_date = date(y1, m1, d1)
    due_date = date(y2, m2, d2)
    if (returned_date == due_date) or (returned_date < due_date):
        fine = 0
        return fine
    if ((returned_date.day) > (due_date.day)) and (returned_date.month == due_date.month) and (returned_date.year == due_date.year):
        fine = (15 * (returned_date.day - due_date.day))
        return fine
    if ((returned_date.month) > (due_date.month)) and (returned_date.year == due_date.year):
        fine = (500 * (returned_date.month-due_date.month))
        return fine
    if (returned_date.year > due_date.year):
        fine = 10000
        return fine
