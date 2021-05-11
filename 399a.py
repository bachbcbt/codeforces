r=input().split('+')
a=0
b=0
for k in range(len(r),0,-1):
    for i in range(0,k-1):
        a=r[i]
        b=r[i+1]
        if int(r[i])>=int(r[i+1]):
            r[i]=b
            r[i+1]=a
print('+'.join(r))