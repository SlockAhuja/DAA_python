def quicksort(arr, low, high):
    #divide
    if low<high:
        pi=partion(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
def partion(arr, low, high):
    #finding the pivot element:conquer
    pivot= arr[high]
    left= low
    right= high-1
    
    while left<=right:
        while left<=right and arr[left]<=pivot:
            left+=1
        while left<=right and arr[right]>=pivot:
            right-=1
        if left<right:
            arr[left],arr[right]=arr[right],arr[left]   
    arr[left],arr[high]=arr[high],arr[left]
    return left         

arr=[10,7,9,3,2,0,7,5,4]
quicksort(arr,0,len(arr)-1)
print("Sorted array is:",arr)