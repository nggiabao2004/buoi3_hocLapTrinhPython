

import math

x=0
y=0

while True:
    print("UP, DOWN, LEFT, RIGHT")
    lenh = input("Nhap huong di chuyen va so buoc (VD: UP 5), ket thuc bang ENTER: ")
    if not lenh:
        break
    huong, buocDi = lenh.split()
    buocDi = int(buocDi)

    if huong.upper() == "UP":
        y+= buocDi
    elif huong.upper() == "DOWN":
        y-= buocDi
    elif huong.upper() == "LEFT":
        x-= buocDi
    elif huong.upper() == "RIGHT":
        x+= buocDi

khoangCach = math.sqrt(x**2 + y**2)
print("Khoang cach tu tam 0 den vi tri hien tai la:", round(khoangCach))