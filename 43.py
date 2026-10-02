#  Find the second smallest number in a tuple. 

tuple1=(1,3,5,7,2,4,6)

sum1=tuple(sorted(tuple1))
sum2=sum1[1]
print(sum2)  #2
print(type(sum1)) #<class 'tuple'>