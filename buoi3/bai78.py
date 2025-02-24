def printSquareValues():
    squareDict={}
    for i in range(1, 21):
        squareDict[i] = i**2
    #Dictionary: dinh nghia khai niem
    #VD: (NAME, AGE)= (Van A, 20)
    #Ta co the phan tach trong phan tu Dict duoc dinh nghia truoc do
    #Truong hop bai nay chi lay gia tri (Value)
    for value in squareDict.values():
        print(value)

if __name__ == "__main__":
    printSquareValues()