list1=[i for i in range (1,11)]
list2=map(lambda y:bin(y)[2:],filter(lambda x:x%2==0,list1))
print(list2)