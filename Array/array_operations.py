
"""
Array operations
append()
insert()
pop()
remove()
index()
reverse()
"""
import array
arr = array.array('i',[1,2,3,4,5,6,7,8])
print("Original Array:",arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\r")

# using append () to  insert value at end
# arr.append(4)
# Array insert(i,x) Method by indexes
# arr.insert(0,5)
# using pop() to remove element at nth index position
# arr.pop(2)
# Array remove() it will the exact value
# arr.remove(4)
# Array index() it will find the index of the value
# print(arr.index(2))
# Array reversed function
arr.reverse()
for i in range(len(arr)):
    print(arr[i],end=" ")

# Array insert(i,x) Method