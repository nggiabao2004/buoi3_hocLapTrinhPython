#tao va mang rong
#dung vong lap while de nhap tung gia tri vao mang
#list1=[1,2,3,4,5,6,7,8,9,0]
#filter(lambda x:x%2==0,list1)
#iterable 2,4,6 -> 4,16,36
#map(lambda y:y**2,filter(lambda x:x%2==0,list1))

list=[1,2,3,4,5,6,7,8,9,0]
listChan=list(filter(lambda x:x%2==0,list))
listBinhPhuong=list(map(lambda y:y**2,listChan))

print(listBinhPhuong)