def LinearSearch(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1



arr = [10,20,50,30,90,40,60]
n = len(arr)
x = int(input())

results = LinearSearch(arr,n,x)

if results == -1:
    print("item not in array")
else:
    print("intem in index:: ",results)

