list1=[5,6,77,45,22,12,24]
list_new=[]
#list_new=[i for i in list1 if i%2==0]

for i in list1:
    if i%2==0:
        list_new.append(i)
print(list_new)