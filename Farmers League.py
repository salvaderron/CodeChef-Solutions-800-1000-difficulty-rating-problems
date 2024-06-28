# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    first=3*(x-1)
    if (x-2)%2==0:
        sec=3*((x-2)/2)
    else:
        sec=3*(((x-2)+1)/2)
    print(int(first-sec))
