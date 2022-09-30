n=int(input())
cat=0
apple=1
ball=1
if n==0 or n==1:
    print("Yes")
else:
    while cat<n:
        cat=apple+ball
        ball=apple
        apple=cat
    if cat==n:
        print("True")
    else:
        print("False")