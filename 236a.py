s=input()
list1=list(s)
list2=[]
for i in range(0,len(list1)):
    if list2.count(list1[i])==0:
        list2.append(list1[i])
if len(list2)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')