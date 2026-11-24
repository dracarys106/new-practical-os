# Practical 06 — Configured, Free and Used Memory Information

[Back to Index](../README.md)

## Practical Question

**Write a program to report behaviour of Linux kernel including information on configured memory, amount of free and used memory (Memory information).**

## Aim

To display total, free, available and used system memory using Linux memory information.

## Requirements

- Linux operating system.
- Python 3.

## Python Program

File: [`../code/p06_memory_info.py`](../code/p06_memory_info.py)

```python
def read_meminfo():
    memory = {}

    with open("/proc/meminfo", "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.split(":", 1)
            # Values in /proc/meminfo are generally given in kB.
            parts = value.strip().split()
            if parts and parts[0].isdigit():
                memory[key] = int(parts[0]) * 1024

    return memory


def to_mb(byte_value):
    return byte_value / (1024 * 1024)


try:
    mem = read_meminfo()

    total = mem.get("MemTotal", 0)
    free = mem.get("MemFree", 0)
    available = mem.get("MemAvailable", free)
    used = total - available

    print("LINUX MEMORY INFORMATION")
    print("------------------------")
    print(f"Configured / Total memory : {to_mb(total):.2f} MB")
    print(f"Free memory               : {to_mb(free):.2f} MB")
    print(f"Available memory          : {to_mb(available):.2f} MB")
    print(f"Estimated used memory     : {to_mb(used):.2f} MB")

except (OSError, ValueError) as error:
    print("Unable to read memory information:", error)
```

## Explanation

- `/proc/meminfo` provides memory statistics maintained by the Linux kernel.
- `MemTotal` represents total usable RAM reported by the kernel.
- `MemFree` is completely unused memory.
- `MemAvailable` estimates memory available for starting new applications without swapping.
- Estimated used memory is calculated here as `MemTotal - MemAvailable`.
- The values are converted from bytes to megabytes for display.

## How to Run

```bash
python3 code/p06_memory_info.py
```

## Result

The configured, free, available and estimated used memory of the Linux system were displayed.

## Important Details

- `MemFree` and `MemAvailable` are not the same. Linux uses otherwise-unused RAM for caches and buffers.
- The program uses `MemTotal - MemAvailable` as an estimate of memory in use; it is not identical to every tool's definition of used memory.
- `/proc/meminfo` is Linux-specific.
