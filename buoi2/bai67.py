#1010 (ma nhi phan)= 0+2^0 + 1*2^1 + 0*2^2 + 1*2^3 (lam tu phai -> trai)= 10 (ma thap phan)
#0100, 0011, 1010, 1001
#cat chuoi
#for duyet qua mang
#thap_phan=int(1,2)
#thap_phan chia 5= 0

#Nhap chuoi: 0100,0011,1010,1001
chuoi=input("Nhap chuoi ma nhi phan: ")
mangSo=[]
#cat chuoi
mang=chuoi.split(",")
for i in mang:
    so_thap_phan=int(i,2)
    #int(i,2) la chuyen sang thanh so (int), cung la 'ma thap phan' tu 'ma nhi phan'
    if so_thap_phan%5==0:
        mangSo.append(i)
print(",".join(mangSo))