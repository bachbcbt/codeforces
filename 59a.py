s=input()
list1=list(s)
test=0
for i in range(0,len(list1)):
    if list1[i].isupper()==True:
        test=test+1
    else:
        test=test-1
if test>0:
    s=s.upper()
else:
    s=s.lower()
print(s)