if __name__ == '__main__':
    n = int(input())
    revnum = []
    for i in range(n+1):
        revnum.append(i)

    revnum.pop(0)
    print(*revnum, sep="")