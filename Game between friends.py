# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if a>b:
        b=b+c
    elif b>a:
        a=a+c
    else:
        a=a+c
    if a>b:
        b=b+d 
    elif b>a:
        a=a+d 
    else:
        b=b+d
    if a>b:
        print("N")
    elif b>a:
        print("S")
    else:
        print("N")
