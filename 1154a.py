s1=input().split()
a=int(s1[0])
b=int(s1[1])
c=int(s1[2])
d=int(s1[3])
sum=max(a,b,c,d)
m=[]
for i in range(0,4):
    if int(s1[i])!=sum:
        m.append(int(s1[i]))
n1=int((m[0]+m[1]-m[2])/2)
n2=int((m[1]+m[2]-m[0])/2)
n3=int((m[0]+m[2]-m[1])/2)
print(n1,n2,n3,sep=' ')