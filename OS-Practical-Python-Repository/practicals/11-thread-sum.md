# Practical 11 — Sum of n Numbers Using Threads

[Back to Index](../README.md)

## Practical Question

**Write a program to calculate sum of n numbers using Pthreads.**

## Aim

To calculate the sum of a list of numbers using a separate thread.

## Python Implementation Note

The question names **Pthreads**, the POSIX threads API commonly used in C. This repository uses Python's built-in `threading` module to demonstrate the same basic idea of creating a thread, performing work in it and waiting for it to finish. It is not a direct Pthreads API implementation.

## Python Program

File: [`../code/p11_thread_sum.py`](../code/p11_thread_sum.py)

```python
import threading

numbers = []
result = {}

def calculate_sum(values):
    result["sum"] = sum(values)
    print("Sum calculated inside worker thread:", result["sum"])


n = int(input("Enter how many numbers: "))

for i in range(n):
    value = int(input(f"Enter number {i + 1}: "))
    numbers.append(value)

worker = threading.Thread(target=calculate_sum, args=(numbers,))
worker.start()
worker.join()

print("Main thread: worker has finished.")
print("Final sum:", result["sum"])
```

## Explanation

- `threading.Thread()` creates a new thread.
- `target` specifies the function executed by the thread.
- `args` passes the list of numbers to the function.
- `start()` starts the worker thread.
- `join()` makes the main thread wait until the worker finishes.
- The result is stored in a shared dictionary.

## How to Run

```bash
python3 code/p11_thread_sum.py
```

## Result

A worker thread was created to calculate the sum of n numbers, and the main thread waited for its completion.

## Important Details

- Python `threading` is used here instead of the POSIX Pthreads API.
- `join()` is important because it waits for the worker thread to complete.
- The program accepts integer inputs. It can also be adapted for floating-point values by using `float()`.
