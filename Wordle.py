# cook your dish here
n=int(input())
for i in range(0,n):
    s=input()
    t=input()
    m=""
    for j in range(0,len(s)):
        if (s[j]==t[j]):
            m=m+"G"
        else:
            m=m+"B"
    print(m)
