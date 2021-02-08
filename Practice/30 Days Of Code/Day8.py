# Dictionaries and Maps
if __name__ == '__main__':  # Code by Vertika Dhingra.
    n = int(input())  # Input1: no. of entries in the phonebook.

    # Input2: names and phonenumber using dictionary comprehension.
    phonebook = {name: int(phonenumber) for name, phonenumber in (
        input().split() for _ in range(n))}
    # print(phonebook)

    # Input3: must continue reading lines until there is no more input.
    try:
        query = []
        while True:
            query.append(input())  # taking input and storing it in a list.
    except EOFError:
        pass

    for x in query:  # iterating over the user entered queries.
        # printing the associated value(phonenumber) to the key(name),if it exists.
        if x in phonebook:
            print(x, '=', phonebook.get(x), sep='')
        else:
            # printing not found , if it doesn't exists.
            print('Not found')
