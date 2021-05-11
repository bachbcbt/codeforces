s=input().split()
n=int(s[0])
t=int(s[1])
list1=list(input())
for i in range(1,t+1):
    temp=0
    for j in range(0,n-1):
        if temp==0 and list1[j]=='B' and list1[j+1]=='G':
            temp=1
            list1[j]='G'
            list1[j+1]='B'
        else:
            temp=0
print(''.join(list1))