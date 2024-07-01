# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    holi=list(map(int,input().split()))
    for j in range(1,31):
        if (j%7==0):
            holi.append((j))
        elif (j%7==6):
            holi.append((j))
        else:
            pass
    holi.sort()
    set1=set(holi)
    print(len(set1))
