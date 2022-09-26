r=int(input())
sum = 0
for i in range(1, r):
    if(r % i == 0):
        sum = sum + i
if(sum==r):
  print(True)
else:
    print(False)