# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    ans=0
    for j in range(1,x+1):
        if j%2==0:
            ans-=1
        else:
            ans+=3
    print(ans)
