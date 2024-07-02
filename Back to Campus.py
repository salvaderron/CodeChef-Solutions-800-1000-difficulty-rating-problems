# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    count=0
    while(a>0):
        a=a-b
        count+=1
    print(count)
