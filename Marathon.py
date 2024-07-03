# cook your dish here
n=int(input())
for i in range(0,n):
    D,d,a,b,c=map(int,input().split())
    km=D*d
    if km>=10 and km<21:
        print(a)
    elif km>=21 and km<42:
        print(b)
    elif km>=42:
        print(c)
    else:
        print(0)
