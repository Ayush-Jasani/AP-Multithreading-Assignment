
# 🧵 Multithreading Tasks in Python

This project demonstrates the use of **multithreading** in Python to improve performance in sorting algorithms and file downloading. It includes three separate tasks:

---

## 1. 🔀 Multithreaded Merge Sort

A classic merge sort algorithm enhanced with Python threads to sort two halves of the array in parallel.

### How it works:
- Splits the array into left and right halves.
- Creates two threads for sorting each half concurrently.
- Merges the sorted halves back together.

### Run:
```python
main_merge()
```

---

## 2. ⚡ Multithreaded Quicksort

An efficient implementation of quicksort that creates two threads for recursively sorting left and right sub-arrays.

### How it works:
- Chooses a pivot and partitions the array.
- Launches threads to sort sub-arrays concurrently.
- Joins threads to merge results.

### Run:
```python
main_quick()
```

---

## 3. 🌐 Concurrent File Downloader

Downloads multiple files simultaneously using threads.

### How it works:
- Accepts a list of file URLs.
- Spawns one thread per download task.
- Downloads all files concurrently and saves them locally.

### Run:
```python
main_download()
```

---

## ✅ Requirements
- Python 3.6+
- `requests` module (for the downloader)
  
Install dependencies:
```bash
pip install requests
```

---
