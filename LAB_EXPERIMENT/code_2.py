#selection sort

def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]#swapping the minimum index

arr=[3,2,5,78,5,2,5,7,2,1,8]
selectionsort(arr)
print(arr)

