n=int(input())
s=input().split()
sum=0
for i in range(0,n):
    sum=sum+int(s[i])
if sum==0:
    print('EASY')
else:
    print('HARD')