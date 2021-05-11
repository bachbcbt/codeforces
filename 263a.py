r=[]
for i in range(1,6):
    r.append(input().split())
for i in range(1,6):
    for j in range(1,6):
        if r[i-1][j-1]=='1':
            count=abs(3-i)
            count=count + abs(3-j)
print(count)
