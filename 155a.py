n=int(input())
s=input().split()
min=int(s[0])
max=int(s[0])
sum=0
for i in range(1,n):
    if int(s[i])<min:
        min=int(s[i])
        sum=sum+1
    if int(s[i])>max:
        max=int(s[i])
        sum=sum+1
print(sum)