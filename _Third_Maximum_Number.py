n=int(input())
l=[int(i) for i in input().split()]
x=[]
for i in l:
    if i not in x:
        x.append(i)
if len(x)>=3:
    print(x[2])
else:
    print(x[len(x)-1])