n=int(input())
s=input()
list1=list(s)
a=list1[0]
count=0
for i in range(1,n):
    if a==list1[i]:
        count=count+1
        a=list1[i]
    else:
        a=list1[i]
print(count)