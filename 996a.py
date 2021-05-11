n=int(input())
sum=0
l=[100,20,10,5,1]
for i in range(0,len(l)):
    sum=sum+int(n/l[i])
    n=n%l[i]
    if n==0:
        break
print(sum)