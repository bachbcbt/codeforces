s=input().split()
n=int(s[0])
k=int(s[1])
time=0
for i in range(1,n+1):
    time=time+i*5
    if 240-time<k:
        print(i-1)
        break
    if i==n:
        print(n)