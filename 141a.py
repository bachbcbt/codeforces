s1=input()
s2=input()
s3=list(input())
s12=s1+s2
check1=set(s12)
check2=set(s3)
sum=0
if check1!=check2:
    print('NO')
else:
    for i in check2:
        if s3.count(i)!=s12.count(i):
            print('NO')
            break
        else:
            sum=sum+1
    if sum==len(check2):
        print('YES')