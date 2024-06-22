# cook your dish here
a,b=map(str,input().split())
if a==b:
    print(a)
elif a=='G':
    if b=='B':
        print("B")
    else:
        print("R")
elif a=="B":
    if b=="G":
        print("B")
    else:
        print("R")
else:
    print("R")
