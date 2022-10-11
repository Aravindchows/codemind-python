import math;
def fun(n):
    for i in range(2,sqrt(n)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if fun(n):
    print("prime")
else:
    print("not a prime")