a=int(input())
n=input()
c=0
for i in n:
    if i=='.':
        c+=1
if c>a//2:
    print("YES")
    for i in n:
        if i=='.':
            print("B",end="")
        else:
            print(i,end="")
else:
    print("NO")