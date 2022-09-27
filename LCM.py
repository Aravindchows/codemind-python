num1,num2=map(int,input().split())
if(num1>num2):
    maximum=num1
else:
    maximum=num2
while(True):
    if(maximum %num1 == 0 and maximum %num2 == 0):
        print(maximum)
        break;
    maximum = maximum + 1