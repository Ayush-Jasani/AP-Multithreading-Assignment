import sys
sys.setrecursionlimit(10000)

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        left = threading.Thread(target=quicksort, args=(arr, low, pi - 1))
        right = threading.Thread(target=quicksort, args=(arr, pi + 1, high))

        left.start()
        right.start()
        left.join()
        right.join()

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main_quick():
    import time
    import random
    arr = [random.randint(0, 10000) for _ in range(10000)]
    start = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end = time.time()
    print("Multithreaded Quicksort completed in", end - start, "seconds")