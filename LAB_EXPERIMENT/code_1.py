#insertion sort

def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
arr=[3,2,5,78,5,2,5,7,2,1,8]
insertionsort(arr)
print(arr)