n=int(input())
l=[int(i) for i in input().split()]
ans=s=l[0]
for i in range(1,n):
    s=max(l[i],s+l[i])
    ans=max(ans,s)
print(ans)