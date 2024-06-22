# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if b>a:
        print((a+((b-a)-1)+b))
    else:
        print((b+((a-b)-1))+a)
        
        
