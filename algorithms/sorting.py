import random

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
           if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def optimized_bubbleSort(arr):
    # uses last exchange index to determine if array is sorted
    n = len(arr) - 1
    while n > 0:
        lastExchangeIndex = 0 

        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                lastExchangeIndex = i

        # set n to last exchange index
        # continue sorting the sublist arr[0] to arr[n]
        n = lastExchangeIndex

    # basically sort sublists before LEI
    return arr

unsorted_list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", unsorted_list)
print("Bubble Sort: ", bubbleSort(unsorted_list))
print("Optimized Bubble Sort: ", optimized_bubbleSort(unsorted_list))
print()

def insertionSort(arr):
    # start from 1 since we assume arr[0] is already sorted
    # insert arr[i] into the sorted sublist arr[0] to arr[i-1]
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

unsorted_list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", unsorted_list)
print("Insertion Sort: ", insertionSort(unsorted_list))
print()

def merge(left, right): 
    ret = []

    while left and right: 
        if left[0] < right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))
    if left:
        ret.extend(left)
    if right:
        ret.extend(right)
    return ret

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))

unsorted_list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", unsorted_list)
print("Merge Sort: ", mergeSort(unsorted_list))
print()

# Quick Sort explanation 
# divide and conquer algorithm
# 1. choose a pivot element
# 2. partition the array such that all elements less than pivot are to the left and all elements greater than pivot are to the right
# 3. recursively sort the left and right subarrays
def partition(arr, low, high): 
    pivot = arr[high]
    j = low 

    for i in range(low, high): 
        if arr[i] <= pivot: 
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j

def quickSort(arr, low, high): 
    if low < high: 
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr
    
unsorted_list = [random.randint(0, 100) for i in range(10)]
print("Unsorted list: ", unsorted_list)
print("Quick Sort: ", quickSort(unsorted_list, 0, len(unsorted_list) - 1))
