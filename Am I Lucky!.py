# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    g=a-b
    tb=int(b/c)
    b=b-(tb*c)
    tg=int(g/c)
    g=g-(tg*c)
    bon=min(b,g)
    rem=(b+g)-(2*bon)
    print(rem)
