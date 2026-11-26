def min_max(arr,start,end):
    if start==end:
        return arr[start],arr[start]
    elif end==start+1:
        if arr[start]<arr[end]:
            return arr[start],arr[end]
        else:
            return arr[end],arr[start]
    else:
        mid=(start+end)//2
        min1,max1=min_max(arr,start,mid)
        min2,max2=min_max(arr,mid+1,end)
        return min(min1,min2),max(max1,max2)