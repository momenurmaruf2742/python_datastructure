# Deleting Elements
'''''To delete elements, use the del keyword which is built-in into Python but this does not return anything back to us.
If you want the element back, you use the pop() function which takes the index value.
To remove an element by its value, you use the remove() function.'''''

my_list=[1,2,3,4,'maruf',5,6]
del my_list[5] #delete element at index 5
print(my_list)
my_list.remove('maruf') #remove element with value
print(my_list)
a = my_list.pop(1) #pop element from list
print('Popped Element: ', a, ' List remaining: ', my_list)
my_list.clear() #empty the list
print(my_list)