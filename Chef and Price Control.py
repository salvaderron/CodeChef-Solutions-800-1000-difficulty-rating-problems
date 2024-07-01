# cook your dish here
n=int(input())
for i in range(0,n):
    x,k=map(int,input().split())
    arr=list(map(int,input().split()))
    brevenue=sum(arr)
    for j in range(0,len(arr)):
        if (arr[j]>k):
            arr[j]=k
    arevenue=sum(arr)
    print(brevenue-arevenue)
