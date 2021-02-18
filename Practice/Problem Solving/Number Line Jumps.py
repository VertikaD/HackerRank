# Complete the kangaroo function below.
# 17/30 test cases passed.
# code by Vertika Dhingra.
def kangaroo(x1, v1, x2, v2):
    if (x2>x1 and v2>v1) or (x1>x2 and v1>v2):
        return 'NO'
    else:
        try:
            jump=0
            while x1!=x2:
                jump+=1
                x1+=v1
                x2+=v2

            return 'YES'
        except:
            return 'NO'