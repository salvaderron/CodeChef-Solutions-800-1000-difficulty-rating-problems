# cook your dish here
n=int(input())
for i in range(0,n):
    reverse=0
    x=int(input())
    temp=x
    while(x!=0):
        digit = x  % 10
        reverse = reverse * 10 + digit
        x //= 10
    if reverse==temp:
        print("wins")
    else:
        print("loses")
