# cook your dish here
import math
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    print(round(math.sqrt(2*(a-b))))
