# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    count=0
    for j in range(0,x):
        a,b=map(int,input().split())
        if (b-a)>5:
            count+=1
    print(count)
