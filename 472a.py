s1=input().split()
n=int(s1[0])
a=4
check=True
def test(a):
    for i in range(2,a):
        if a%i==0:
            return True
    return False
while (check==True):
    if test(a)==True:
        b=n-a
        if test(b)==True:
            check=False
            print(a,b)
    a=a+1
