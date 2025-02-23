mang=[]
while True:
    line=input("Nhap noi dung vao, va ket thuc bang ENTER: ")
    #Kt dong co noi dung
    if line:
        mang.append(line.upper())
    #Kt dong ko co noi dung
    else:
        break
for i in mang:
    print(i)