list1=[]
value=0
for i in range (1,20):
    value+=1
    list1.append(int(value))

listChan=list(filter(lambda x:x%2==0,list1))
print(listChan)