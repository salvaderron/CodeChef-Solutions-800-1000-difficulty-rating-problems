# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count=0
    start_time = 0
    
    for j in range(x):
        available_time = a[j] - start_time
        if b[j] <= available_time:
            count += 1
        start_time = a[j]
    
    print(count)
