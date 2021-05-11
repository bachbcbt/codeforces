s=input()
s1=list(s)
count=0
for i in range(0,len(s1)):
    if s1[i]=='4' or s1[i]=='7':
        count=count+1
count1=list(str(count))
if (count1.count('4') + count1.count('7'))==len(count1):
    print('YES')
else:
    print('NO')