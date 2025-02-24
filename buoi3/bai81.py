def listSquare():
    list=[]
    for i in range (1,21):
        list.append(i**2)
    #Lay khoang trong list [soDauLayTrongMang:soCuoiLayTrongMang]
    #truong hop so am thi lay tu cuoi day (phai) sang trai de tim gia tri mang[-i]
    print(list[-5:])

if __name__ == "__main__":
    listSquare()