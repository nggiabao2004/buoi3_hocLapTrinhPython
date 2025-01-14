import math
# Tạo mảng rỗng
list1= []

# Sử dụng vòng lặp while để nhập giá trị
while True:
    try:
        so=int(input())
        list1.append(so)
    except ValueError:
        break

#viet hamkiem tra so chinh phuong
def timSoChinhPhuong(x):
    # lay can cua
    # bien=int(lay can)
    y=int(math.sqrt(x))
    # neu bien*bien=x
    if y*y==x:
        return True
    else:
        return False
    
listSoChinhPhuong= list(filter(timSoChinhPhuong,list1))
print(listSoChinhPhuong)