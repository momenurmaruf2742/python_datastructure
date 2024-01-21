# Accessing Elements
# Accessing elements is the same as accessing Strings in Python. You pass
# the index values and hence can obtain the values as needed.
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list: #access elements one by one
    print(element)
print(my_list) #access all elements
print(my_list[3]) #access index 3 element
print(my_list[0:2+1]) #access elements from 0 to 1 and exclude 2
print(my_list[::-1]) #access elements in reverse
