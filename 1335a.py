n=int(input())
l=[]
for i in range(0,n):
    l.append(input())
for i in range(0,n):
    k=0
    if int(l[i])>=2:
        if int(l[i])%2==0:
            k=int(int(l[i])/2)-1
        else:
            k=int(int(l[i])/2)
    print(k)