# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    arr=list(map(int,input().split()))
    count=0
    res=1
    for j in range(0,len(arr)):
        if arr[j]<0:
            count+=1
        res=res*arr[j]
    if res>=0:
        print(0)
    else:
        if count%2!=0:
            print(1)
