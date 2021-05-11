n=list(input())
n.pop(0)
n.pop(-1)
if len(n)>=2:
    n1=''.join(n)
    n2=n1.split(', ')
    s=set(n2)
else:
    s=set(n)
print(len(s))
