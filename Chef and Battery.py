# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    ans=0
    if x==50:
        print(0)
    else:
        while(x!=50):
            if x<50:
                x+=2
            else:
                x-=3
            ans+=1
        print(ans)
