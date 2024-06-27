# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c,d,e=map(int,input().split())
    supply=min((a/c),(b/d))
    if (supply>=e):
        print("YES")
    else:
        print("NO")
