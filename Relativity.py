# cook your dish here
n=int(input())
for i in range(0,n):
    g,c=map(int,input().split())
    print(int((c*c)/(2*g)))
