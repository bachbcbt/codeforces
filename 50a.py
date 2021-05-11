w1=input()
l1=w1.split()
m=int(l1[0])
n=int(l1[1])
count=0
if m%2==0:
    a=m 
else:
    a=m-1
    count=count+int(n/2)
if n%2==0:
    b=n 
else:
    b=n-1
    count=count+int(m/2)
count=count+(a*b/2)
print(int(count))
