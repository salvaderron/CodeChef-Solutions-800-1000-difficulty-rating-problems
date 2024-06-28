# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    runs=list(map(int,input().split()))
    count=0
    run=runs[0]
    t=1
    for j in range(0,len(runs)):
        srate=(run/(j+1))*100
        if (t!=x):
            run=run+runs[t]
        t+=1
        if srate==100.0:
            count+=1
    print(count)
