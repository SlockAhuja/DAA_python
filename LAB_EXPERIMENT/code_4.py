#linear search



def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr=[3,2,5,78,5,2,5,7,6,1,8]
key=789
result=linear_search(arr, key)

if(result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)