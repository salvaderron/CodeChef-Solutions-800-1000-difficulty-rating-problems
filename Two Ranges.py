# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    arr=[]
    for j in range(a,b+1):
        arr.append(j)
    for k in range(c,d+1):
        arr.append(k)
    set1=set(arr)
    print(len(set1))
