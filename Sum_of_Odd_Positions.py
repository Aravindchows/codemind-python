n=int(input())
a=list(map(int,input().split()))
o=[]
for x in range(len(a)):
    if x%2!=0:
        o.append(a[x])
print(sum(o))