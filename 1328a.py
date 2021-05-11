n=int(input())
l=[]
for i in range(0,n):
    s=input().split()
    l.append(s)

for i in range(0,n):
    a=int(l[i][0])
    b=int(l[i][1])
    if a%b==0:
        print('0')
    else:
        k=int(a/b)+1
        a2=b*k
        plus=a2-a
        print(plus)
