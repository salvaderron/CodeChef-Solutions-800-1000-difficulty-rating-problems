# cook your dish here
n=int(input())
for i in range(0,n):
    h,cc,ts=map(float,input().split())
    if h>50 and cc<0.7 and ts>5600:
        print(10)
    elif (h>50 and cc<0.7):
        print(9)
    elif (cc<0.7 and ts>5600):
        print(8)
    elif (h>50 and ts>5600):
        print(7)
    elif (h>50 or cc<0.7 or ts>5600):
        print(6)
    else:
        print(5)
