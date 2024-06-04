#quicksort algorthim
import numpy as np

#quicksort algorthim

def quicksort(arr, left, right):
    if left < right:
        partition_pos, count = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right )
        return count

def partition(arr, left, right):
    count = 0
    pivot = arr[left]

    start = left + 1
    end = right
    while True:
        count += 1
        while start <= end and arr[end] >= pivot:
            end -= 1
            count += 1
        count += 1
        while start <= end and arr[start] <= pivot:
            start += 1
            count += 1
        if start <=  end:
            count += 1
            arr[start], arr[end] = arr[end], arr[start]
        else: break
    arr[left], arr[end] = arr[end], arr[left]
    return end, count

def generate_random_input(size):
    arr = np.random.randint(0, 20000, size = size)
    return arr

array = [7, 6, 10, 5, 9, 2, 1, 15, 7]
count = quicksort(array, 0, len(array) - 1)
print(array)
print(count)


