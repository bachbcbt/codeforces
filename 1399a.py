t=int(input())
for a in range(0,t):
    n=int(input())
    s1=input().split()
    if n==1:
        print('YES')
    else:
        for i in range(0,n):
            s1[i]=int(s1[i])
        s2=sorted(s1)
        for i in range(0,n-1):
            if (s2[i+1]-s2[i])>=2:
                print('NO')
                break
            elif i==n-2:
                print('YES')
