import re

mang=[]
while True:
    chuoi=input()
    if chuoi:        
        mang.append(chuoi)
    else:
        break
mangMoi=list(filter(lambda word:word.startswitch(('a','b')),mang))
print(",".join(mangMoi))