if __name__ == '__main__':  # Code by Vertika Dhingra.
    n = int(input())
    integer_list = map(int, input().split())
    # tuple takes iterable and here we are passing a list to tuple .
    t = tuple(integer_list)
    print(hash(t))
