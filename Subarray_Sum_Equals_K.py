a,b=map(int,input().split())
m=list(map(int,input().split()))
c=0
s=0
for i in range(0,a):
    for j in  range(i,a):
        s+=m[j]
        if s==b:
            c+=1
        if s>b:
            break
    s=0
print(c)