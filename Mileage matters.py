# cook your dish here
z=int(input())
for i in range(0,z):
    n,x,y,a,b=map(int,input().split())
    if ((x/a)*n)>((y/b)*n):
        print("DIESEL")
    elif ((x/a)*n)<((y/b)*n):
        print("Petrol")
    else:
        print("ANY")
    
