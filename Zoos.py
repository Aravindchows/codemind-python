n=input()
c=0
d=0
for i in n:
    if i=='z':
        d+=1
    else:
        c+=1
if 2*d==c:
    print('Yes')
else:
    print('No')