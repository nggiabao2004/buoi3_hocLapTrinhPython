def divide():
    try:
        result = 5/0
    except ZeroDivisionError:
        print("Khong chia het cho 0")
    else:
        print("Ket qua la: ", result)

if __name__ == "__main__":
    divide()