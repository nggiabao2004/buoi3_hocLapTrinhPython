#map duoc su dung de ap dung len tung phan tu cua iterable
#map(function, iterable,... )
#function: ham nay duoc ap dung len tung phan tu cua iterable

number=[1,2,3,4,5]
listNew=list(map(lambda x:x**2,number))
print(listNew)