#Bubble sort

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        boolean=False
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if(swapped==False):
            break

arr=[3,2,5,78,5,2,5,7,2,1,8]
bubblesort(arr)
print(arr)