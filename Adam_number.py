n=int(input())
s=n*n
s1=0
s2=0
while(n>0):
 w=n%10
 s1=s1*10+w
 n=n//10
f1=s1*s1
while(f1>0):
    a=f1%10
    s2=s2*10+a
    f1=f1//10
if(s==s2):
    print("True")
else:
    print("False")
    