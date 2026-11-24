# Practical 07 — Copy Files Using System Calls

[Back to Index](../README.md)

## Practical Question

**Write a program to copy files using system calls.**

## Aim

To copy the contents of one file into another using low-level file system calls in Python.

## Requirements

- Python 3.
- Linux or another operating system supporting the required `os` file operations.

## Python Program

File: [`../code/p07_copy_file.py`](../code/p07_copy_file.py)

```python
import os
import sys

def copy_file(source, destination):
    source_fd = None
    destination_fd = None

    try:
        source_fd = os.open(source, os.O_RDONLY)
        destination_fd = os.open(
            destination,
            os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
            0o644
        )

        while True:
            data = os.read(source_fd, 4096)
            if not data:
                break

            view = memoryview(data)
            while view:
                written = os.write(destination_fd, view)
                view = view[written:]

        print("File copied successfully.")

    finally:
        if source_fd is not None:
            os.close(source_fd)
        if destination_fd is not None:
            os.close(destination_fd)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 code/p07_copy_file.py source destination")
        sys.exit(1)

    copy_file(sys.argv[1], sys.argv[2])
```

## Explanation

- `os.open()` opens a file and returns a file descriptor.
- `os.read()` reads a block of bytes from the source file.
- `os.write()` writes bytes to the destination file.
- `os.close()` closes the file descriptors.
- The loop continues until `os.read()` returns empty bytes, indicating end of file.
- The inner loop handles partial writes so that all bytes are written.

## How to Run

```bash
python3 code/p07_copy_file.py input.txt output.txt
```

Check the copied file:

```bash
cat output.txt
```

## Result

The contents of the source file were copied to the destination file using low-level file operations.

## Important Details

- Give the source and destination as command-line arguments.
- The destination is created if it does not exist and overwritten if it already exists.
- Do not use the same path for source and destination; doing so can truncate the source.
- `finally` ensures that opened file descriptors are closed even if an error occurs.
