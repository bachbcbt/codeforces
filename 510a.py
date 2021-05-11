s=input().split()
n=int(s[0])
m=int(s[1])
i=1
while i<=n:
    if i%4==1:
        print('#'*m)
    if i%4==2:
        print(('.'*(m-1))+'#')
    if i%4==3:
        print('#'*m)
    if i%4==0:
        print('#'+('.'*(m-1)))
    i=i+1
