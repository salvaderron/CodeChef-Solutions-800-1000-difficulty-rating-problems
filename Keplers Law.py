# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    if ((a*a)/(c*c*c))==((b*b)/(d*d*d)):
        print("Yes")
    else:
        print("No")
