# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    if x%10==0:
        print(0)
    else:
        x=x*2
        if x%10==0:
            print(1)
        else:
            print(-1)
