# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    print(min(abs(b-a),min(c-a+b,c-b+a)))
