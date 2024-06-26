# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    arr=[]
    for j in range(a,b+1):
        if (j%10==2):
            arr.append(j)
        elif (j%10==3):
            arr.append(j)
        elif (j%10==9):
            arr.append(j)
    print(len(arr))
