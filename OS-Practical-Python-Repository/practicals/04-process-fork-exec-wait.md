# Practical 04 — Parent and Child Processes Using fork(), exec() and wait()

[Back to Index](../README.md)

## Practical Question

**Write a program (using `fork()` and/or `exec()` commands) where parent and child execute:**

1. Same program, same code.
2. Same program, different code.
3. Before terminating, the parent waits for the child to finish its task.

## Aim

To demonstrate process creation, execution of parent and child code, and synchronization using Python's process-related system calls.

## Requirements

- Linux or another Unix-like operating system.
- Python 3.
- Run from a terminal. Standard Windows Python does not support `os.fork()`.

## Program 1 — Same Program, Same Code

File: [`../code/p04_fork_same_code.py`](../code/p04_fork_same_code.py)

```python
import os

pid = os.fork()

if pid == 0:
    print("Child process")
    print("Child PID:", os.getpid())
    print("Child's parent PID:", os.getppid())
else:
    print("Parent process")
    print("Parent PID:", os.getpid())
    print("Child PID returned by fork():", pid)
    os.waitpid(pid, 0)
    print("Parent: child has completed.")
```

### Explanation

- `os.fork()` creates a child process.
- It returns `0` in the child process.
- It returns the child's PID in the parent process.
- Both processes continue from the statement after `fork()`, so they execute the same program but can follow different branches.
- `os.waitpid(pid, 0)` makes the parent wait for that child.

## Program 2 — Same Program, Different Code Using exec()

File: [`../code/p04_fork_exec_different_code.py`](../code/p04_fork_exec_different_code.py)

```python
import os
import sys

pid = os.fork()

if pid == 0:
    print("Child: replacing child process with another Python program.")
    os.execv(sys.executable, [sys.executable, "-c",
                              "print('Child: executing different code using exec.')"])
else:
    print("Parent: waiting for child.")
    os.waitpid(pid, 0)
    print("Parent: child has completed.")
```

### Explanation

- `fork()` first creates a child process.
- The child calls `os.execv()`.
- `execv()` replaces the child process's program with the specified Python command.
- The parent continues independently and waits for the child using `os.waitpid()`.

## Program 3 — Parent Waits for Child

The `os.waitpid(pid, 0)` statement in both programs demonstrates the required waiting behaviour. The parent prints its completion message only after the child has terminated.

## How to Run

```bash
python3 code/p04_fork_same_code.py
python3 code/p04_fork_exec_different_code.py
```

## Result

The parent and child process behaviour was demonstrated using `fork()`. Different child code was executed using `exec()`, and the parent waited for the child using `waitpid()`.

## Important Details

- Output order can vary because the operating system scheduler decides which process runs first.
- `fork()` duplicates the process; it does not create a new source-code file.
- `exec()` replaces the current process image. It does not create another process.
- `waitpid()` prevents the parent from proceeding until the specified child changes state/terminates.
- This practical is Linux/Unix-specific. Do not run it on standard Windows Python.
