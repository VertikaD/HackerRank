if __name__ == '__main__':
    s = input()

    value1 = []
    value2 = []
    value3 = []
    value4 = []
    value5 = []
    for x in s:
        if x.isalnum():
            value1.append('True')
        else:
            value1.append('False')
        if x.isalpha():
            value2.append('True')
        else:
            value2.append('False')
        if x.isdigit():
            value3.append('True')
        else:
            value3.append('False')
        if x.islower():
            value4.append('True')
        else:
            value4.append('False')
        if x.isupper():
            value5.append('True')
        else:
            value5.append('False')

    if 'True' in value1:
        print('True')
    else:
        print('False')
    if 'True' in value2:
        print('True')
    else:
        print('False')
    if 'True' in value3:
        print('True')
    else:
        print('False')
    if 'True' in value4:
        print('True')
    else:
        print('False')
    if 'True' in value5:
        print('True')
    else:
        print('False')
