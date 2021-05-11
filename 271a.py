year=int(input())
check=True
while(check):
    year=year+1
    year2=list(str(year))
    sum=0
    for i in range(0,4):
        if year2.count(year2[i])>1:
            sum=sum+1
    if sum==0:
        print(''.join(year2))
        check=False
