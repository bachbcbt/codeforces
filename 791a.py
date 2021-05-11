s=input().split()
a=int(s[0])
b=int(s[1])
i=1
while True:
    x=a*(3**i)
    y=b*(2**i)
    if x>y:
        print(i)
        break
    i=i+1