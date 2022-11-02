n=int(input())
a=list(map(int,input().split()))
e=[]
for x in range(len(a)):
    if x%2==0:
        e.append(a[x])
print(sum(e))