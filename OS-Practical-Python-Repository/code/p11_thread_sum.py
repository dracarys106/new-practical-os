import threading

numbers = []
result = {}


def calculate_sum(values):
    result["sum"] = sum(values)
    print("Sum calculated inside worker thread:", result["sum"])


n = int(input("Enter how many numbers: "))
if n < 0:
    raise SystemExit("Number of values cannot be negative.")

for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

worker = threading.Thread(target=calculate_sum, args=(numbers,))
worker.start()
worker.join()

print("Main thread: worker has finished.")
print("Final sum:", result["sum"])
