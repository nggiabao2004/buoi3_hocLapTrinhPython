# hello;anh;c
# -> anh c hello

chuoi=input("Nhap vao chuoi: ")
#Bo dau ";"
chuoi_moi=chuoi.split(";")
#loai bo khoang trang va sap xep theo bang chu cai
sort_chuoi=sorted(i.strip() for i in chuoi_moi)
#them dau "," vao sort_chuoi
ketqua=",".join(sort_chuoi)
print(ketqua)