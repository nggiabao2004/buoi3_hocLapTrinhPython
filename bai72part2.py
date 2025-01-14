#tao mang rong
list=[]
while True:
    number=input("Nhap 1 chu so: ")
    if number=="":
        break
    elif number.isdigit():
        list.append(number)

list_new=[]
#list_new=[i for i in list1 if i!=24]

for i in list:
    if i!=24:
        list_new.append(i)
print(list_new)