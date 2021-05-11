s=list(input())
s1=list(input())
s2=[]
for i in range(1,len(s)+1):
    s2.append(s[-i])
if s1==s2:
    print('YES')
else:
    print('NO')