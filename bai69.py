#cần có chuỗi
#duyệt qua
#nếu ký tự là số: isdigit() đếm số
#nếu ký tự là chữ: isalpha() đếm ký tự
#ngược lại đếm ký tự đặc biệt
#in các biến đếm

text=input("Nhap chuoi ky tu: ")

numString= 0
charString= 0
specialString= 0

for char in text:
    if char.isalpha():
        charString += 1
    elif char.isdigit():
        numString += 1
    else:
        specialString += 1

print("So chu cai la: ", charString)
print("So chu so la: ",numString)
print("So ki tu dac biet: ", specialString)