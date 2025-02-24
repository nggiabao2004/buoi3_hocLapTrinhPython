def square(num):
    return num**2

listNum= list(range(1,21))
listNew= list(map(square,listNum))
print(listNew)