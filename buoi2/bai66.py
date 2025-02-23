# #tap hop (Set): la 1 tap hop, ko co thu tu, ko chua phan tu trung lap
# #va cac phan tu co the thay the dc
# #tao tap {} 
# set1={1, 2, 3}
# set2=set([3,4,5,6])
# #cac thao tac co ban
# set1.add(7)
# set1.add(7) #ko cong don trung lap
# print(set1)
# #remove
# # | giao, & hop, - hieu
# print(set1|set2)
# print(set1&set2)
# print(set1-set2)

# #---</>---
chuoi=input("Nhap chuoi ki tu: ")
mang=set(chuoi.split())
mang_sx=sorted(mang)
for i in mang_sx:
    print(i)