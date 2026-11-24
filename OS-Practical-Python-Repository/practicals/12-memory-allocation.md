# Practical 12 — First-Fit, Best-Fit and Worst-Fit Memory Allocation

[Back to Index](../README.md)

## Practical Question

**Write a program to implement first-fit, best-fit and worst-fit allocation strategies.**

## Aim

To simulate the First-Fit, Best-Fit and Worst-Fit memory allocation strategies.

## Theory

- **First-Fit:** Allocates a process to the first memory block large enough to hold it.
- **Best-Fit:** Allocates a process to the smallest available block that is large enough.
- **Worst-Fit:** Allocates a process to the largest available block that is large enough.

In this program, each block's remaining size is reduced after allocation. A process is allocated to at most one block.

## Python Program

File: [`../code/p12_memory_allocation.py`](../code/p12_memory_allocation.py)

```python
def allocate(blocks, processes, strategy):
    remaining = blocks[:]
    allocation = [-1] * len(processes)

    for i, process_size in enumerate(processes):
        candidates = [
            j for j, block_size in enumerate(remaining)
            if block_size >= process_size
        ]

        if not candidates:
            continue

        if strategy == "first":
            chosen = candidates[0]
        elif strategy == "best":
            chosen = min(candidates, key=lambda j: remaining[j])
        elif strategy == "worst":
            chosen = max(candidates, key=lambda j: remaining[j])
        else:
            raise ValueError("Unknown allocation strategy")

        allocation[i] = chosen
        remaining[chosen] -= process_size

    return allocation, remaining


def display(name, blocks, processes, allocation, remaining):
    print(f"\\n{name}")
    print("Process\\tSize\\tBlock")
    for i, size in enumerate(processes):
        if allocation[i] == -1:
            print(f"P{i + 1}\\t{size}\\tNot allocated")
        else:
            print(f"P{i + 1}\\t{size}\\tB{allocation[i] + 1}")

    print("Remaining block sizes:", remaining)


block_count = int(input("Enter number of memory blocks: "))
blocks = []

for i in range(block_count):
    blocks.append(int(input(f"Enter size of block {i + 1}: ")))

process_count = int(input("Enter number of processes: "))
processes = []

for i in range(process_count):
    processes.append(int(input(f"Enter size of process {i + 1}: ")))

for strategy, title in [
    ("first", "FIRST-FIT"),
    ("best", "BEST-FIT"),
    ("worst", "WORST-FIT")
]:
    allocation, remaining = allocate(blocks, processes, strategy)
    display(title, blocks, processes, allocation, remaining)
```

## How to Run

```bash
python3 code/p12_memory_allocation.py
```

## Result

First-Fit, Best-Fit and Worst-Fit memory allocation strategies were simulated and their allocations were displayed.

## Important Details

- Each strategy starts with a fresh copy of the original memory blocks so that the results can be compared fairly.
- A block's remaining size is reduced after a process is allocated.
- `-1` internally means that a process was not allocated; the output displays “Not allocated”.
- This is a simplified variable-size allocation simulation, not a complete operating-system memory manager.
