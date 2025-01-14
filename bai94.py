mang= []
tong=0

while True:
    so=input("Nhap so: ")
    if so=="" or int(so)<0:
        break
    mang.append(int(so))
    
listBinhPhuong=list(map(lambda x:x*x,mang))
listChan=list(filter(lambda x:x%2==0,listBinhPhuong))
for i in listChan:
    tong+=i
print(tong)