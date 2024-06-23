# cook your dish here
n=int(input())
for i in range(0,n):
    arr=list(map(int,input().split()))
    one=arr.count(1)
    zero=arr.count(0)
    if (one>=zero):
        print("YES")
    else:
        print("NO")
