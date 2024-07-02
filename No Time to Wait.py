# cook your dish here
n,h,x=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
for i in range(0,n):
    if (arr[i]+x)>=h:
        ans=1
if ans==0:
    print("NO")
else:
    print("YES")
