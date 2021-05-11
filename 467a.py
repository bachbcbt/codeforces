n=int(input())
sum=0
for i in range(0,n):
    s=input().split()
    if (int(s[1])-int(s[0]))>=2:
        sum=sum+1
print(sum)