# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    a=list(str(int(input())))
    if '0' in a or '5' in a:
        print("Yes")
    else:
        print("No")
