n=int(input())
s=input().split()
sum1=0
sum2=100*len(s)
for i in range(0,len(s)):
    sum1=sum1+int(s[i])
print(sum1*100/sum2)