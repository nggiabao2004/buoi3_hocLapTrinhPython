import re
chuoi=input("Nhap vao chuoi")
print(re.findall(r'\d',chuoi))
# tim kiem voi re.match()
# kiem tra khop voi dau chuoi
# tao mau
pattern=r"Hello"
ketqua=re.match(pattern,chuoi)
if ketqua:
    print("Tim thay: ",ketqua.group())
else:
    print("Khong tim thay")

# tim kiem bat ky vi tri nao voi re.search()
pattern1=r'Python'
ketqua1=re.search(pattern1,chuoi)
if ketqua1:
    print("Tim thay: ",ketqua1.start())
else:
    print("Khong tim thay")

#ham thay the re.sub()
pattern2=r'love'
replace1='yeu'
ketqua2=re.sub(pattern2,replace1,chuoi)
print(ketqua2)

#ham tach chuoi re.split()
pattern3=r"[,;|]"
ketqua4=re.split(pattern3,chuoi)
print(ketqua4)
