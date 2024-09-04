from random import randint 
arr = [randint(0,100) for _ in range(10)]

def insertionsort(arr): 
    n = len(arr) 
    for i in range(1, n): 
        key = arr[i]
        j = i-1 
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

print(insertionsort(arr.copy()))

def partition(arr, low, high):
    pivot = arr[high]
    j = low

    for i in range(low, high): 
        if arr[i] < pivot: 
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[high], arr[j] = arr[j], arr[high]

    return j 

def quicksort(arr, low, high): 
    if low < high: 
        pivot = partition(arr, low, high) 
        quicksort(arr,low, pivot - 1)
        quicksort(arr,pivot +1, high)
    return arr

print(quicksort(arr.copy(), 0, len(arr)-1 ))
