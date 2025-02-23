# Tạo mảng rỗng
list = []

# Sử dụng vòng lặp while để nhập giá trị
while True:
    value = input("Nhập một số vào mảng: ")
    
    # Kiểm tra nếu người dùng muốn thoát
    if value.lower() == '':
        break
    list.append(int(value))

listChan = list(filter(lambda x: x % 2 == 0, list))
listBinhPhuong = list(map(lambda y: y ** 2, listChan))
print("Danh sách các số chẵn đã bình phương:", listBinhPhuong)