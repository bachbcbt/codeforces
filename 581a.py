s=input().split()
a1=int(s[0])
a2=int(s[1])
if a1>a2:
    b1=a1
    b2=a2
    print(b2,int((b1-b2)/2))
elif a1<a2:
    b1=a2
    b2=a1
    print(b2,int((b1-b2)/2))
else:
    print(a1,'0')
