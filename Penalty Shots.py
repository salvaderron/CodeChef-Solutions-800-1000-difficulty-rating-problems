# cook your dish here
n=int(input())
for i in range(0,n):
    arr=list(map(int,input().split()))
    team1=[]
    team2=[]
    for j in range(0,len(arr)):
        if ((j+1)%2==0):
            team2.append(arr[j])
        else:
            team1.append(arr[j])
    one1=team1.count(1)
    one2=team2.count(1)
    if one1>one2:
        print(1)
    elif one2>one1:
        print(2)
    else:
        print(0)
