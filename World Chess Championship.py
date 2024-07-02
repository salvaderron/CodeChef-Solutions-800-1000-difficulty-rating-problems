# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    arr=list(input())
    c=arr.count("C")
    n=arr.count("N")
    d=arr.count("D")
    if c>n:
        print(60*x)
    elif (c==n):
        print(55*x)
    else:
        print(40*x)
