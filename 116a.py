n=int(input())
sum=0
max=0
for i in range(0,n):
    s=input().split()
    a=int(s[0])
    b=int(s[1])
    sum=sum-a+b
    if sum>max:
        max=sum
print(max)



