import math

def up(y):
    buocDi=int(input("Nhap so buoc di UP: "))
    return y + buocDi

def down(y):
    buocDi=int(input("Nhap so buoc di DOWN: "))
    return y - buocDi

def left(x):
    buocDi=int(input("Nhap so buoc di LEFT: "))
    return x - buocDi

def right(x):
    buocDi=int(input("Nhap so buoc di RIGHT: "))
    return x + buocDi

def main():
    x=0
    y=0

    while True:
        print("UP: W")
        print("DOWN: S")
        print("LEFT: A")
        print("RIGHT: D")
        print("EXIT: E")
        luaChon = input("Nhap huong di chuyen: ")
        if luaChon == "W" or luaChon == "w":
            y = up(y)
        elif luaChon == "S" or luaChon == "s":
            y = down(y)
        elif luaChon == "A" or luaChon == "a":
            x = left(x)
        elif luaChon == "D" or luaChon == "d":
            x = right(x)
        elif luaChon == "E" or luaChon == "e" or luaChon=="":
            break
        else:
            print("Khong hop le, vui long nhap lai")

    khoangCach = math.sqrt(x**2 + y**2)
    print("Khoang cach tu tam 0 den vi tri hien tai la:", round(khoangCach))
    
if __name__== "__main__":
    main() #Main chương trình, giống public static void main(String[] args){}
    # Python đọc code từ trên xuống, nên để dòng if __name__== "__main__": này ở dưới