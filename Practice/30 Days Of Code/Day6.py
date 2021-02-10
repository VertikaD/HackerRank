if __name__ == '__main__':  # Code by Vertika Dhingra.
    T = int(input())  # input : number of test cases.
    all_strings = []  # nested list.
    for x in range(T):  # input: multiple strings in the range of test cases.
        # split() is used to take multiple inputs.
        all_strings.append(input().split())

    all_strings_f = [x[0] for x in all_strings]  # list flattening
    # converting 2D list into 1D list.

    for i in all_strings_f:  # looping over the list of strings.
        letter = []
        for s in i:
            letter.append(s)

            even_index = letter[::2]
            odd_index = letter[1::2]

        # this function prints even and odd index with space separated strings.
        def print_singleline(even, odd):
            for t in even:
                print(t, end='')
                # creating space separated strings in a single line.
            print(end=' ')
            for q in odd:
                print(q, end='')

        print_singleline(even_index, odd_index)
        print('\t')
