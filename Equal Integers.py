# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif b>a:
        print(b-a)
    else:
        if (a-b)%2==0:
            print((a-b)//2)
        else:
            print((a-b)//2+2)
            
                
                
