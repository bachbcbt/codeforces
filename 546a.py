s=input().split()
cost=int(s[0])
money=int(s[1])
need=int(s[2])
sum=0
for i in range(1,need+1):
    sum=sum+i*cost
if money<sum:
    print(sum-money)
else:
    print('0')