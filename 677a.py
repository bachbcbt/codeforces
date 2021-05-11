s1=input().split()
s2=input().split()
sum=0
for i in range(0,len(s2)):
    if int(s2[i])>int(s1[1]):
        sum=sum+2
    else:
        sum=sum+1
print(sum)