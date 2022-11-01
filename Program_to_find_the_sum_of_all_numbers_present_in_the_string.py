string1=input()
sum=0
for i in string1:
    if i.isnumeric():
         sum=sum+int(i)
print(str(sum))
 