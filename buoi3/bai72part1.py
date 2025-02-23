list1=[12,24,35,24,88,120,155]
list_new=[]
#list_new=[i for i in list1 if i!=24]

for i in list1:
    if i!=24:
        list_new.append(i)
print(list_new)