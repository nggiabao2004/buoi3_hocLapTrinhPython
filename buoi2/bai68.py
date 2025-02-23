#In ra day so tu 1000 - 3000
mangSo=[]
for i in range (1000, 3001):
    if i%2==0:
        mangSo.append(str (i))
print(",".join(mangSo))