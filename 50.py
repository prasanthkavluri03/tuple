#  Create a nested tuple containing student name, course, and marks, then display all details. 

tuple1=(("name:","prasanth"),
    ("course:","web deplover"),
    ("marks:",70))
print(type(tuple1)) #<class 'tuple'>

for x in tuple1:
    print(x[0],x[1])    # name: prasanth
                        # course: web deplover
                        # marks: 70