def listSquare():
    list=[]
    for i in range (1,21):
        list.append(i**2)
    listTuple= tuple(list)
    print(listTuple)

if __name__ == "__main__":
    listSquare()