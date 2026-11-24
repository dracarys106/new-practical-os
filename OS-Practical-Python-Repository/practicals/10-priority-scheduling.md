# Practical 10 — Non-Preemptive Priority Scheduling

[Back to Index](../README.md)

## Practical Question

**Write a program to implement non-preemptive priority-based scheduling algorithm.**

## Aim

To implement non-preemptive priority CPU scheduling and calculate waiting time and turnaround time.

## Theory

In priority scheduling, the CPU is allocated to the ready process with the highest priority. In this program, a **smaller priority number represents a higher priority**. Non-preemptive means the selected process runs until it finishes.

- **Turnaround Time = Completion Time − Arrival Time**
- **Waiting Time = Turnaround Time − Burst Time**

## Python Program

File: [`../code/p10_priority.py`](../code/p10_priority.py)

```python
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    print(f"Process P{i + 1}")
    at = int(input("Arrival time: "))
    bt = int(input("Burst time: "))
    priority = int(input("Priority (smaller number = higher priority): "))
    processes.append({
        "pid": f"P{i + 1}",
        "at": at,
        "bt": bt,
        "priority": priority,
        "done": False
    })

current_time = 0
completed = 0
total_wt = 0
total_tat = 0
results = []

while completed < n:
    ready = [
        p for p in processes
        if not p["done"] and p["at"] <= current_time
    ]

    if not ready:
        current_time = min(
            p["at"] for p in processes if not p["done"]
        )
        continue

    # Lowest numeric priority value is selected first.
    selected = min(
        ready,
        key=lambda p: (p["priority"], p["at"], int(p["pid"][1:]))
    )

    current_time += selected["bt"]
    ct = current_time
    tat = ct - selected["at"]
    wt = tat - selected["bt"]

    selected["done"] = True
    completed += 1
    total_wt += wt
    total_tat += tat
    results.append((
        selected["pid"], selected["at"], selected["bt"],
        selected["priority"], ct, tat, wt
    ))

print("\\nPID\\tAT\\tBT\\tPR\\tCT\\tTAT\\tWT")
for row in results:
    print("\\t".join(map(str, row)))

print(f"\\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
```

## How to Run

```bash
python3 code/p10_priority.py
```

## Result

The non-preemptive priority scheduling algorithm was implemented and average waiting and turnaround times were calculated.

## Important Details

- Smaller priority number means higher priority in this program. Some textbooks use the opposite convention; follow the convention stated in your question or by your instructor.
- A process that has started is not interrupted.
- Equal priorities are broken by earlier arrival time, then process number.
- This program does not include aging.
