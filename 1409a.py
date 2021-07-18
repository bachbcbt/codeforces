t=int(input())
for a in range(0,t):
    s1=input().split()
    a=int(s1[0])
    b=int(s1[1])
    if a==b:
        print(0)
    else:
        if (b-a)%10!=0:
            print(int(abs(b-a)/10)+1)
        else:
            print(int(abs(b-a)/10))
