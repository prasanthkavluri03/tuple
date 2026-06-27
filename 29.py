# Remove an element from a tuple by converting it into a list. 

tuple1=(1,2,3,4,5,6,7,8,9,10)
list1=list(tuple1)

print(type(tuple1)) #<class 'tuple'>
print(type(list1)) #<class 'list'>

list1.remove(2)

tuple2=tuple(list1)
print(tuple2) #(1, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(tuple2)) #<class 'tuple'>