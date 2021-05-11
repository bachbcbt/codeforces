n=int(input())
s=input().split()
time=0
min=int(s[0])
max=int(s[0])
# print(s)
for i in range(0,n):
    if int(s[i])>max:
        max=int(s[i])
    if int(s[i])<min:
        min=int(s[i])
for i in range(0,n):
    if int(s[i])==max:
        m1=i
        break
for i in range(n-1,-1,-1):
    if int(s[i])==min:
        m2=n-1-i
        break
if m1+m2>=n:
    time=m1+m2-1
else:
    time=m1+m2
print(time)
