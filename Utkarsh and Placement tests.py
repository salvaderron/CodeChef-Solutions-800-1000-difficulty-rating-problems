# cook your dish here
n=int(input())
for i in range(0,n):
    pre=list(map(str,input().split()))
    rec=list(map(str,input().split()))
    a=0
    for j in range(0,len(pre)):
        for k in range(0,len(rec)):
            if (pre[j]==rec[k]):
                a=1
                break
        if (a==1):
            print(pre[j])
            break
