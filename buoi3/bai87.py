tuple1=(1,2,3,4,5,6,7,8,9)
tupleNew=tuple(x for x in tuple1 if x%2==0)
print(tupleNew)