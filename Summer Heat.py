# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d=map(int,input().split())
    print(int((c/a)+(d/b)))
