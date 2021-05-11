w1=input()
l1=w1.split()
n=int(l1[0])
k=int(l1[1])
count=0
w2=input()
l2=w2.split()
for i in range(0,n):
    if int(l2[i])>=int(l2[k-1]) and int(l2[i])>0:
        count=count+1
print(count)
