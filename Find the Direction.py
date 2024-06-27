# cook your dish here
n=int(input())
for i in range(0,n):
    a=int(input())
    if a%4==0:
        print("North")
    elif a%4==1:
        print("East")
    elif (a%4==2):
        print("South")
    else:
        print("West")
