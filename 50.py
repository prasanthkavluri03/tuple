#  Create a nested tuple containing student name, course, and marks, then display all details. 

t1=(("name:","prasanth"),
    ("course:","web deplover"),
    ("marks:",70))
print(type(t1)) #<class 'tuple'>

for x in t1:
    print(x[0],x[1])    # name: prasanth
                        # course: web deplover
                        # marks: 70