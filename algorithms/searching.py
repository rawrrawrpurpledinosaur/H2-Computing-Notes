import random

random.seed(69)

arr = [random.randint(1, 100) for _ in range(10)]
arr.sort()
print(arr)


def linearSearch(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return f"Found {target} at index {i}"
    return f"{target} not found"


def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def recursiveBinarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    def helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, high)
        else:
            return helper(low, mid - 1)


print(recursiveBinarySearch(arr, 9))

# Ignore below because bad implementation
arr = [0] * 10


def hash_function(n):
    return n % 10


nums = [5, 9, 13, 22, 42, 45, 54, 71, 78, 88]
for num in nums:
    pos = hash_function(num)
    if arr[pos] == 0:
        arr[pos] = num
    else:
        pass
