#  Find the second largest number in a tuple. 


tuple1=(1,2,3,4,5,6,7,8,9)

sum1=tuple(reversed(sorted(tuple1)))

s2=sum1[1]
print(type(sum1)) #<class 'tuple'>
print(s2) #8