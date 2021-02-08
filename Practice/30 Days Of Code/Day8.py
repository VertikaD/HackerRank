# Dictionaries and Maps
if __name__ == '__main__':  # Code by Vertika Dhingra.
    n = int(input())  # Input1: no. of entries in the phonebook.

    # Input2: names and phonenumber using dictionary comprehension.
    phonebook = {name: int(phonenumber) for name, phonenumber in (
        input().split() for _ in range(n))}

    print(phonebook)

    # Input3: Query by user till user wants.

    query = [input() for _ in range(3)]

    for x in query:  # iterating over the user entered queries.
        if x in phonebook:
            print(x+'='+phonebook.get(x), sep='')
        else:
            print('Not found')
