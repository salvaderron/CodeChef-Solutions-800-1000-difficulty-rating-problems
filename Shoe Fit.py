# cook your dish here
n=int(input())
for i in range(0,n):
    arr=list(map(int,input().split()))
    l=arr.count(0)
    r=arr.count(1)
    print(min(l,r))
