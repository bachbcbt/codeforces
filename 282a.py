n=int(input())
x=0
for i in range(0,n):
    w=input()
    if w.count('++')==1:
        x=x+1
    if w.count('--')==1:
        x=x-1
print(x)