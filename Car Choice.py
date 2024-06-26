# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if (c/a)<(d/b):
        print(-1)
    elif (c/a)>(d/b):
        print(1)
    else:
        print(0)
