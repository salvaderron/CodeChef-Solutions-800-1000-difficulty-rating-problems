# cook your dish here
n=int(input())
for i in range(0,n):
    sc1=list(map(int,input().split()))
    sc2=list(map(int,input().split()))
    c1=0
    c2=0
    for j in range(0,len(sc1)):
        if (sc1[j]>sc2[j]):
            c1+=1
        elif (sc2[j]>sc1[j]):
            c2+=1
    if c1>c2:
        print("A")
    else:
        print("B")
