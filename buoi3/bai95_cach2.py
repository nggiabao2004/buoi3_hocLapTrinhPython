import re

mang=[]
pattern=r"^[ab]"
while True:
    chuoi=input()
    if chuoi:
        ketQua=re.findall(pattern,chuoi)
        if ketQua:
            mang.append(chuoi)
    else:
        break
print(",".join(mang))