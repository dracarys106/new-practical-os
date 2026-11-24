# Practical 08 — First Come First Serve (FCFS) Scheduling

[Back to Index](../README.md)

## Practical Question

**Write a program to implement First Come First Serve (FCFS) scheduling algorithm.**

## Aim

To implement FCFS CPU scheduling and calculate waiting time and turnaround time for each process.

## Theory

FCFS is a non-preemptive CPU scheduling algorithm. The process that arrives first gets the CPU first. If two processes have the same arrival time, their input order is used.

- **Turnaround Time (TAT) = Completion Time − Arrival Time**
- **Waiting Time (WT) = Turnaround Time − Burst Time**

## Python Program

File: [`../code/p08_fcfs.py`](../code/p08_fcfs.py)

```python
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    print(f"Process P{i + 1}")
    at = int(input("Arrival time: "))
    bt = int(input("Burst time: "))
    processes.append({
        "pid": f"P{i + 1}",
        "at": at,
        "bt": bt
    })

# Stable sort: preserves input order when arrival times are equal.
processes.sort(key=lambda p: p["at"])

current_time = 0
total_wt = 0
total_tat = 0

print("\\nPID\\tAT\\tBT\\tCT\\tTAT\\tWT")

for p in processes:
    if current_time < p["at"]:
        current_time = p["at"]

    current_time += p["bt"]
    ct = current_time
    tat = ct - p["at"]
    wt = tat - p["bt"]

    total_wt += wt
    total_tat += tat

    print(f'{p["pid"]}\\t{p["at"]}\\t{p["bt"]}\\t{ct}\\t{tat}\\t{wt}')

print(f"\\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
```

## How to Run

```bash
python3 code/p08_fcfs.py
```

## Example Input

```text
Enter number of processes: 3
Process P1
Arrival time: 0
Burst time: 5
Process P2
Arrival time: 1
Burst time: 3
Process P3
Arrival time: 2
Burst time: 2
```

## Example Output

```text
PID     AT  BT  CT  TAT WT
P1      0   5   5   5   0
P2      1   3   8   7   4
P3      2   2   10  8   6

Average Waiting Time: 3.33
Average Turnaround Time: 6.67
```

## Result

The FCFS scheduling algorithm was implemented and average waiting time and turnaround time were calculated.

## Important Details

- AT = Arrival Time, BT = Burst Time, CT = Completion Time.
- FCFS is non-preemptive.
- The CPU remains idle if no process has arrived.
- Enter a positive number of processes and non-negative arrival/burst times. Burst time should be greater than zero.
