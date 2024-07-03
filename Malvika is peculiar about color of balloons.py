# cook your dish here
n=int(input())
for i in range(0,n):
    arr=list(input())
    a=0
    b=0
    a=arr.count("a")
    b=arr.count("b")
    print(min(a,b))
