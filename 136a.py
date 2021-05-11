n=int(input())
give=input().split()
take=[]
for i in range(0,n):
    for j in range(0,n):
        m=i+1
        if int(give[j])==m:
            take.append(str(j+1))
print(' '.join(take))

