# Create a tuple from user input values. 

n=int(input("Enter the number= "))

list1=[]

list1.append(n)
tuple1=tuple(list1)
print(tuple1)  #(66,)
print(type(tuple1)) #<class 'tuple'>