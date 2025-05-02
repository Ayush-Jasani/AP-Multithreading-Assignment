import threading

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        t1 = threading.Thread(target=merge_sort, args=(L,))
        t2 = threading.Thread(target=merge_sort, args=(R,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main_merge():
    import time
    import random
    arr = [random.randint(0, 10000) for _ in range(10000)]
    start = time.time()
    merge_sort(arr)
    end = time.time()
    print("Multithreaded Merge Sort completed in", end - start, "seconds")