n1=list(input())
n2=list(input())
for i in range(0,len(n1)):
    if n1[i]!=n2[i]:
        print('1',end='')
    else:
        print('0',end='')