# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    cp=a*b
    sp=a*c
    print(sp-cp)
