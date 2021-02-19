# Complete the birthday function below.
# code by Vertika Dhingra.
def birthday(s, d, m):
    #finding all contiguous non-empty subarrays. (n*(n+1)/2)
    subarrays=[]
    if len(s)==1:
        subarrays.append(s)
    else:
        for x in range(len(s)):
            for i in range(len(s)-1):
                n = (i+x)+1
                if n<=len(s):
                    subarrays.append(s[i:n])

    r = len([i for i in subarrays if len(i)==m and sum(i)==d ])
    return r


