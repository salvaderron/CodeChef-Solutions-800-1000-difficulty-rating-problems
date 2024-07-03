# cook your dish here
n=int(input())
for i in range(0,n):
    arr=list(map(int,input().split()))
    one=arr.count(1)
    if one==0:
        print("Beginner")
    elif one==1:
        print("Junior Developer")
    elif one==2:
        print("Middle Developer")
    elif one==3:
        print("Senior Developer")
    elif one==4:
        print("Hacker")
    elif one==5:
        print("Jeff Dean")
        
