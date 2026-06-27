#  Find the second largest number in a tuple. 


t1=(1,2,3,4,5,6,7,8,9)

s1=tuple(reversed(sorted(t1)))

s2=s1[1]
print(type(s1)) #<class 'tuple'>
print(s2) #8