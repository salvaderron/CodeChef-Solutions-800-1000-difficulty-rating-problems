n=int(input())
for i in range(0,n):
    x1,x2,x3,v1,v2=map(int,input().split())
    d1=x3-x1
    d2=x2-x3
    t1=d1/v1
    t2=d2/v2
    if t1>t2:
        print("Kefa")
    elif t2>t1:
        print("Chef")
    else:
        print("Draw")
