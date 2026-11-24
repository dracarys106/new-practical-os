# Operating Systems Practicals (DSC08) — Python

A GitHub-ready practical record based on the **Suggested Practical List for the Operating System Paper (DSC08)**.

> **Language note:** All programming practicals are written in Python. Linux command demonstrations remain Linux shell commands because the question specifically asks you to execute Linux commands. Practical 4 uses `os.fork()`, `os.execv()` and `os.waitpid()` and therefore requires a Unix-like operating system such as Linux. Python's `threading` module is used for the threads practical.

## Index

Click any practical to jump to its question, explanation, commands or code.

| No. | Practical question | Open |
|---:|---|---|
| 1 | Demonstration of various Operating System functions using OS Simulator | [Practical 01](practicals/01-os-simulator.md) |
| 2 | Execute Linux information, file and directory management commands | [Practical 02](practicals/02-linux-basic-commands.md) |
| 3 | Execute Linux process control, communication and protection commands | [Practical 03](practicals/03-linux-process-commands.md) |
| 4 | Parent and child process execution using fork/exec; parent waits for child | [Practical 04](practicals/04-process-fork-exec-wait.md) |
| 5 | Report Linux kernel version, CPU type and CPU information | [Practical 05](practicals/05-kernel-cpu-info.md) |
| 6 | Report configured, free and used memory | [Practical 06](practicals/06-memory-info.md) |
| 7 | Copy files using system calls | [Practical 07](practicals/07-copy-file-system-calls.md) |
| 8 | Implement First Come First Serve (FCFS) scheduling | [Practical 08](practicals/08-fcfs-scheduling.md) |
| 9 | Implement Shortest Job First (SJF) scheduling | [Practical 09](practicals/09-sjf-scheduling.md) |
| 10 | Implement non-preemptive priority scheduling | [Practical 10](practicals/10-priority-scheduling.md) |
| 11 | Calculate sum of n numbers using threads | [Practical 11](practicals/11-thread-sum.md) |
| 12 | Implement first-fit, best-fit and worst-fit allocation | [Practical 12](practicals/12-memory-allocation.md) |

## Repository structure

```text
OS-Practical-Python-Repository/
├── README.md
├── practicals/
│   ├── 01-os-simulator.md
│   ├── 02-linux-basic-commands.md
│   ├── 03-linux-process-commands.md
│   ├── 04-process-fork-exec-wait.md
│   ├── 05-kernel-cpu-info.md
│   ├── 06-memory-info.md
│   ├── 07-copy-file-system-calls.md
│   ├── 08-fcfs-scheduling.md
│   ├── 09-sjf-scheduling.md
│   ├── 10-priority-scheduling.md
│   ├── 11-thread-sum.md
│   └── 12-memory-allocation.md
└── code/
    ├── p04_fork_same_code.py
    ├── p04_fork_exec_different_code.py
    ├── p05_kernel_cpu_info.py
    ├── p06_memory_info.py
    ├── p07_copy_file.py
    ├── p08_fcfs.py
    ├── p09_sjf.py
    ├── p10_priority.py
    ├── p11_thread_sum.py
    └── p12_memory_allocation.py
```

## Requirements

- Python 3.8 or later (Python 3.10+ recommended).
- Linux for the Linux-command practicals and the `fork/exec` practical.
- A terminal to run the programs.
- No third-party Python package is required by the supplied programs.

Check Python:

```bash
python3 --version
```

Run a program from the repository's root directory:

```bash
python3 code/p08_fcfs.py
```

## Important implementation notes

1. **Practical 1:** The supplied question does not name a particular OS simulator. Follow the simulator provided by your instructor/lab and record the screens/results for the functions demonstrated.
2. **Practicals 2 and 3:** Execute commands in a Linux terminal. These are shell commands, not Python statements.
3. **Practical 4:** `os.fork()` and `os.waitpid()` are Unix-specific and are not available on standard Windows Python. Run these programs on Linux.
4. **Practicals 5 and 6:** The programs read Linux information from `/proc`. They are intended for Linux.
5. **Practical 7:** Uses low-level `os.open`, `os.read`, `os.write` and `os.close` calls to demonstrate file copying.
6. **Practical 11:** Uses Python's `threading` module. This demonstrates concurrent thread execution; it is not the POSIX `pthread` API.
7. Scheduling programs use simple, non-preemptive models. For SJF and priority scheduling, the ready processes are selected when the CPU becomes free. Priority convention in Practical 10: **smaller number = higher priority**.

## How to upload to GitHub

1. Sign in to GitHub and create a new repository, for example `OS-Practicals-Python`.
2. Extract this ZIP file.
3. Open the extracted folder and upload its contents to the new repository, or use Git:

```bash
git init
git add .
git commit -m "Add Operating Systems practicals in Python"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/OS-Practicals-Python.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not include the outer ZIP file itself inside the repository unless you want to keep it as an archive.
