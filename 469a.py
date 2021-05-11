n=int(input())
s1=input().split()
s1.pop(0)
s2=input().split()
s2.pop(0)
w=1
for i in range(1,n+1):
    if s1.count(str(i))==0 and s2.count(str(i))==0:
        w=0
        break
if w==0:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')