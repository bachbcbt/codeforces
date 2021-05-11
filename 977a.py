s=input().split()
a=int(s[0])
b=int(s[1])
k=1
while k<b+1:
    if a%10==0:
        a=a/10
    else:
        a=a-1
    k=k+1
print(int(a))
