# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    ch=a+c*10
    cf=b+d*10
    if ch>cf:
        print("Chefina")
    elif ch<cf:
        print("Chef")
    else:
        print("Draw")
