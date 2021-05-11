w1=input()
w1=w1.lower()
w2=input()
w2=w2.lower()
n=len(w1)
test=0
for i in range(0,n):
    if w1[i]==w2[i]:
        test=0
    if w1[i]>w2[i]:
        test=1
        break
    if w1[i]<w2[i]:
        test=-1
        break
print(test)