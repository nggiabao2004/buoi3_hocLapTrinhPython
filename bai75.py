#nhap vao chuoi
mang=input().strip().split(" ")
#[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19','80')]

list_new=[]
for i in mang:
    name,age,score=i.split(",")
    list_new.append(name,int(age),int(score))
list_sort=sorted(list_new,key=lambda x:(x[0],x[1],x[2]))
print(list_sort)