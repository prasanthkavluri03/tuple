#  Find the second smallest number in a tuple. 

t1=(1,3,5,7,2,4,6)

s1=tuple(sorted(t1))
s2=s1[1]
print(s2)  #2
print(type(s1)) #<class 'tuple'>