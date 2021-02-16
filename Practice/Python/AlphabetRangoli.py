# code by Vertika Dhingra.
import string
# width = N = no. of rows
size = 5
N = (size*2)-1
n = int(N/2)

# Creating the Mid line.
pattern = string.ascii_lowercase[:size]
pattern_rev = pattern[::-1]

# inserting '-' in between the alphabets.
p0 = pattern[0]
for i in pattern[1:]:
    p0 += '-' + i

p1 = pattern_rev[0]
for i in pattern_rev[1:]:
    p1 += '-'+i

mid = p1+p0[1:]

# approach/logic
# this remains constant throughout the iteration.
len_mid = len(mid)
len_mid_half = int(len_mid/2)

Second_Half = []

# Creating the Second Half Pattern.


def Alphabet_Rangoli(AR):

    c = AR.replace(AR[len_mid_half:(len_mid_half+4)], '')
    result = c.center(len(mid), '-')
    Second_Half.append(result)

    R = all(i == '-' for i in result)
    if R == True:
        return None
    else:
        Alphabet_Rangoli(result)


Alphabet_Rangoli(mid)
Second_Half.pop()

# printing the first Half.
for x in Second_Half[::-1]:
    print(x)

# printing the middle part.
print(mid)

# printing the Second Half.
for x in Second_Half:
    print(x)
