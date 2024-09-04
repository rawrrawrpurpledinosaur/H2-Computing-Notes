from random import randint 
arr = [randint(0,100) for i in range(10)]

def insertionSort(arr): 
    n = len(arr)
    for i in range(1, n): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr 


print(insertionSort(arr.copy()))

def partition(arr, low, high):
    # set pivot as high unless specified by the question
    pivot = arr[high]
    # j is "stack" pointer
    j = low
    
    for i in range(low, high): 
        if arr[i] <= pivot: 
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        arr[j], arr[high] = arr[high], arr[j]
    return j

def quickSort(arr, low, high): 
    if low < high: 
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high) 
    return arr


print(quickSort(arr.copy(), 0, len(arr)-1))

