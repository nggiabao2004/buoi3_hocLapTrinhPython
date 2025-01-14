#filter duoc su dung loc cac phan tu trong 1 iterable(list, set, double)
#dua tren 1 dieu kien dinh nghia cua ham
#filter(function, iterable)
#function: ham tra ve gia tri True or False cho tung phan tu
#iterable: 1 tap hop du lieu nhu danh sach, tuple, set, string
#ket qua tra ve cung la iterable, nhu vay can phai chuyen ve list

number=[1,2,3,4,5,6,7,8,9,10]
def timChan(x):
    return x%2==0
listNew= list(filter(timChan,number))
print(listNew)
