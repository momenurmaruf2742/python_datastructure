#adding  data in list
"""The append() function adds all the elements passed to it as a single element.
The extend() function adds the elements one-by-one into the list.
The insert() function adds the element passed to the index value and increase the size of the list too.
"""
my_list=[1,2,3,4,'maruf',5,6]
my_list.append([1256,'new data'])
print(my_list)
my_list.extend([456,'change data'])
print(my_list)
my_list.insert(1,'insert example')
print(my_list)
