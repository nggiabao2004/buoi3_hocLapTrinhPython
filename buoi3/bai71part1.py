#nhap vao 1 chuoi, kiem tra chuoi do co phai la email hop le ko
import re
chuoi=input("Nhap email: ")

pattern=r'^\w+@[a-z A-Z 0-9_-]+\.\w{2,3}$'
if re.match(pattern, chuoi):
    print("Email hop le")
else:
    print("email khong hop le")