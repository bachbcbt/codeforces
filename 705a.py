n=int(input())
i=1
l=[]
while i<=n:
    if i%2!=0:
        l.append('I hate')
    else:
        l.append('I love')
    i=i+1
print(' that '.join(l),'it')