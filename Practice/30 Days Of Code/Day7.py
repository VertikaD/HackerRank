# Arrays
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr)
    reverse_array = list(reversed(arr))
    [print(x, end=' ') for x in reverse_array] # list comprehension.
