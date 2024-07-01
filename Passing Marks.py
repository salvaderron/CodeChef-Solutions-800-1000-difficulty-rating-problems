# cook your dish here
n=int(input())
for i in range(0,n):
    am,bm,cm,tm,a,b,c=map(int,input().split())
    if (a>=am) and (b>=bm) and (c>=cm):
        if(a+b+c)>=tm:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
