#mang rong
#while true:
#   nhap chuoi
#   neu chuoi co gia tri:
#       dua vao mang
#   nguoc lai thi thoat ra
#filter(lambda x:do dai cua x>=3, mang)
#map(lambda,iterable)

mang= []

# Sử dụng vòng lặp while để nhập giá trị
while True:
    chuoi=input()
    if chuoi:
        mang.append(chuoi)
    else:
        break
    
#viet hamkiem tra so chinh phuong

listNew= list(map (str.upper, filter(lambda x:len(x)>=3,mang)))
print(listNew)