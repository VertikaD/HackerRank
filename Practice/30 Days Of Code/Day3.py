# Intro to Conditional Statements.
if __name__ == '__main__':  # Code by Vertika Dhingra.
    N = int(input())
    if (N % 2 != 0):
        print('Weird')
    elif (N % 2 == 0):
        if N >= 2 and N <= 5:
            print('Not Weird')
        if N >= 6 and N <= 20:
            print('Weird')
        if N > 20:
            print('Not Weird')
