number= int(input())
s = number**2
sum=0
while s:
   sum=sum+(s%10)
   s=s//10
if sum==number:
    print("Neon Number")
else:
    print("Not Neon Number")