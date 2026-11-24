# Practical 05 — Linux Kernel and CPU Information

[Back to Index](../README.md)

## Practical Question

**Write a program to report behaviour of Linux kernel including kernel version, CPU type and CPU information.**

## Aim

To display the Linux kernel version, machine architecture and CPU information using Python.

## Requirements

- Linux operating system.
- Python 3.

## Python Program

File: [`../code/p05_kernel_cpu_info.py`](../code/p05_kernel_cpu_info.py)

```python
import platform

print("LINUX KERNEL AND CPU INFORMATION")
print("--------------------------------")
print("Operating system:", platform.system())
print("Kernel release:", platform.release())
print("Kernel version:", platform.version())
print("Machine architecture:", platform.machine())
print("Processor:", platform.processor() or "Not reported by platform module")
print("Logical CPU count:", __import__("os").cpu_count())

# Read detailed CPU information from Linux proc filesystem.
try:
    with open("/proc/cpuinfo", "r", encoding="utf-8") as file:
        cpu_info = file.read()

    print("\\nDetailed CPU information (first processor entry):")
    first_entry = cpu_info.split("\\n\\n")[0]
    print(first_entry)
except OSError as error:
    print("Could not read /proc/cpuinfo:", error)
```

## Explanation

- `platform.system()` identifies the operating system.
- `platform.release()` returns the kernel release.
- `platform.version()` returns the kernel version string.
- `platform.machine()` reports the machine architecture, such as `x86_64`.
- `os.cpu_count()` reports the number of logical CPUs detected.
- `/proc/cpuinfo` contains detailed processor information on Linux.

## How to Run

```bash
python3 code/p05_kernel_cpu_info.py
```

## Sample Output

Output depends on the computer. A typical Linux system may display:

```text
LINUX KERNEL AND CPU INFORMATION
--------------------------------
Operating system: Linux
Kernel release: 6.x.x
Kernel version: ...
Machine architecture: x86_64
Processor: ...
Logical CPU count: 8
```

## Result

The Linux kernel version, CPU architecture and available CPU information were displayed successfully.

## Important Details

- The sample output is illustrative; your system will show its actual values.
- `/proc/cpuinfo` is a virtual Linux system file, not an ordinary saved file.
- CPU model information may vary by processor and Linux environment.
