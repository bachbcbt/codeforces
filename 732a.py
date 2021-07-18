s1=input().split()
k=int(s1[0])
r=int(s1[1])
check=True
i=1
while (check==True):
    if (k*i-r)%10==0:
        check=False
    elif (k*i)%10==0:
        check=False
    else:
        i=i+1
print(i)