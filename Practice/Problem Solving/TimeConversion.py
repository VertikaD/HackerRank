# Complete the timeConversion function below.
# code by Vertika Dhingra.
def timeConversion(s):
    # Write your code here.
    # There are no changes to be done in seconds and minutes.
    # converting 12 hour to 24 hour clock.

    # if last two elements is PM and first two elements are not '12',
    # then add 12 to hour and remove PM.
    if s[-2:] == 'PM' and s[:2] != '12':
        return str(int(s[:2])+12) + s[2:(len(s)-2)]
    # if last two elements is AM and first two elements are not '12',
    # remove AM and return the sliced string.
    if s[-2:] == 'AM' and s[:2] != '12':
        return s[0:(len(s)-2)]

    # Exceptions.
    # 1. if first two elements are 12 and last two elements are 'AM'.
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:(len(s)-2)]
    # 2. if first two elements are 12 and last two elements are 'PM'.
    if s[-2:] == 'PM' and s[:2] == '12':
        return s[0:(len(s)-2)]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
