# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if ((a+b)%2==0):
        print("Bob")
    else:
        print("Alice")
