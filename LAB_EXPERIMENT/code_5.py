#binary search

def binary_search(arr,low,high,key):
    if(low>high):
        return -1
    mid=(low+high)//2
    if(arr[mid]==key):
        return mid
    elif(arr[mid]>key):
        return binary_search(arr,low,mid-1,key)
    else:
        return binary_search(arr,mid+1,high,key)
    
arr=[1,3,5,7,9,11,13,15]
key=13
result=binary_search(arr,0,len(arr)-1,key)
if(result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)



