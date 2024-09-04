from random import randint 

arr = [randint(0,100) for _ in range(10)]

def insertionsort(arr): 
    n = len(arr) 
    for i in range(1, n): 
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = key 
    return arr

print(insertionsort(arr))
