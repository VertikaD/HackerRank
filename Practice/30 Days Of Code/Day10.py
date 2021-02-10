# Binary Numbers
if __name__ == '__main__':  # Code by Vertika Dhingra
    n = int(input())
    Binary_list = []

    def DecimaltoBinary(num):
        if num >= 1:  # we are dividing num by 2 until quotient is >= 1.
            # recursive function because it is repetitive process.
            # calling itself and passing quotient in each division as a parameter.
            DecimaltoBinary(num//2)
            Binary_list.append(num % 2)  # storing remainder to a list.

    Binary = DecimaltoBinary(n)

    # Printing a maximum number of consecutive 1's in the binary representation of n .

    # converting list of binary numbers into string using join and list comprehension.
    Binary_string = ''.join([str(x) for x in Binary_list])

    # 1. .split('0') : creates substrings of consecutive 1's separated by 0's and storing it in a list.
    # 2. map function maps len func. on each substring of consecutive 1's.
    # 3. Finally, max() returns the len of consecutive 1's which is maximum.
    print(max(map(len, Binary_string.split('0'))))
