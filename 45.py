#  Count how many even and odd numbers are present in a tuple. 


t1=(0,1,2,3,4,5,6,7,8,9,10)
even=0
odd=0

for x in t1:
    if x%2==0:
        even=even+1

    else:
        odd=odd+1

print(even) #6
print(odd) #5   