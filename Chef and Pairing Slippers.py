# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    l=a-b
    print(min(l,b)*c)
