def binarysearch(arr, l, r, x):
    if r >= l :
        mid = l + (r-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr,mid+1,r,x)
        else:
            return binarysearch(arr,l,mid-1,x)
    else:
        return -1



arr = [10,20,30,40,50 ]
x=30
result = binarysearch(arr,0,len(arr)-1,x)
if result != -1:
    print("item in index number:",result)
else:
    print("item not in list")

