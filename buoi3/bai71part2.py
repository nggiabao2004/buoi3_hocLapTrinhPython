#nhap vao 1 chuoi, kiem tra chuoi do co phai la so dien thoai hop le ko
import re
chuoi=input("Nhap so dien thoai: ")

pattern=r'^(09|08|03|\+84)\d{8}$'
if re.match(pattern, chuoi):
    print("So dien thoai hop le")
else:
    print("So dien thoai khong hop le")