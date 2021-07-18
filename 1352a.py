t=int(input())
for a in range(0,t):
    s1=list(input())
    for i in range(0,len(s1)):
        s1[i]=int(s1[i])
    s2=[]
    x=0
    for k in range(len(s1)-1, -1, -1):
        s2.append(s1[x]*(10**k))
        x=x+1
    s2=[s for s in s2 if s!=0]
    print(len(s2))
    print(*s2)
