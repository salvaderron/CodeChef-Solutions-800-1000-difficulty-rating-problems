# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if a%2==0:
        if a-1==b or a+2==b or a-2==b:
            print("YES")
        else:
            print("NO")
    elif a%2!=0:
        if a-2==b or a+1==b or a+2==b:
            print("YES")
        else:
            print("NO")
    elif b%2==0:
        if b+1==a or b+2==a or b-2==a:
            print("YES")
        else:
            print("NO")
    else:
        if b-2==a or b+1==a or b+2==a:
            print("YES")
        else:
            print("NO")
        
