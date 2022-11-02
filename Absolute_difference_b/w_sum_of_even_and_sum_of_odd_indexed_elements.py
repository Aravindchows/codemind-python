n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for x in range(len(a)):
    if x%2==0:
        e.append(a[x])
    if x%2!=0:
        o.append(a[x])
print(sum(e)-sum(o))