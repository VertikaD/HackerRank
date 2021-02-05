if __name__ == '__main__':
    N = int(input())
    list = []
    commands = []
    for i in range(0, N):  # list created of the commands entered by the user.
        command = input().lower().split(' ')  # handling case sensitivity
        # here split method is converting string into list
        commands.append(command)


for c in commands:
    if c[0] == 'print':
        print(list)
    if c[0] == 'sort':
        list.sort()
    if c[0] == 'pop':
        list.pop()
    if c[0] == 'reverse':
        list.reverse()

    elif len(c) == 3:
        Zero = int(c[1])
        One = int(c[2])
        list.insert(Zero, One)

    else:
        if c[0] == 'append':
            Two = int(c[1])
            list.append(Two)

        elif c[0] == 'remove':
            Three = int(c[1])
            list.remove(Three)
