#counting sort algorithm implementation in python

def countingsort(arr):
    max_element = max(arr)
    
    count_array = [0] * (max_element + 1)

    for num in arr:
        count_array[num] += 1

    index = 0
    for i in range(len(count_array)):
        while count_array[i] > 0:
            arr[index] = i
            index += 1
            count_array[i] -= 1
    return arr

arr=[2,4,1,2,4,7,5,3,2,5,0,8,12,4,7,3,8,6,9]
countingsort(arr)
print(arr)