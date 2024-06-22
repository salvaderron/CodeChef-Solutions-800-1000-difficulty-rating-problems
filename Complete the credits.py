# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    if x>65:
        print("Overload")
    elif x<35:
        print("Underload")
    else:
        print("Normal")
