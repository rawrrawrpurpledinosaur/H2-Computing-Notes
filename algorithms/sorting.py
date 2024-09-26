from random import randint


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubblesort_optimized(arr):
    # Uses last exchange index to check if array is already sorted
    n = len(arr) - 1
    while n > 0:
        last_exchange_index = 0
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_exchange_index = i
        n = last_exchange_index
    return arr


def insertionsort(arr):
    # Assume first element is sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements within arr[0..i-1] that are greater than key to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr


def test_sorting():
    arr = [randint(0, 100) for i in range(10)]
    print("Original array:", arr)
    print("Bubble sort:", bubblesort(arr.copy()))
    print("Insertion sort:", insertionsort(arr.copy()))
    print("Merge sort:", mergesort(arr.copy()))
    print("Quick sort:", quicksort(arr.copy(), 0, len(arr) - 1))


test_sorting()
