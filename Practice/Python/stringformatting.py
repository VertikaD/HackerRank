# your code goes here
# code by Vertika Dhingra.
def print_formatted(number):
    # your code goes here
    # the maximum length would be of binary .
    # so to correct the alignment , we will set the width of this pattern
    # to be of length of binary conversion of the input given.
    width_binary = bin(number)
    width = width_binary[2:]
    width_len = len(width)
    for i in range(1, number+1):
        decimal = i
        print((str(decimal).rjust(width_len, ' ')), end=' ')
        octal = oct(i)
        print((octal[2:].rjust(width_len, ' ')), end=' ')
        hexadecimal_caps = format(i, '0X')
        print((hexadecimal_caps.rjust(width_len, ' ')), end=' ')
        binary = bin(i)
        print(binary[2:].rjust(width_len, ' '))


print_formatted(int(input()))
