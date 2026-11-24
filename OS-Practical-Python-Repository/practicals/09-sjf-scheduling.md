# Practical 09 — Shortest Job First (SJF) Scheduling

[Back to Index](../README.md)

## Practical Question

**Write a program to implement Shortest Job First (SJF) scheduling algorithm.**

## Aim

To implement non-preemptive SJF scheduling and calculate waiting time and turnaround time.

## Theory

In non-preemptive SJF, whenever the CPU becomes free, the ready process with the smallest burst time is selected. Once selected, it runs until completion.

- **Turnaround Time = Completion Time − Arrival Time**
- **Waiting Time = Turnaround Time − Burst Time**

## Python Program

File: [`../code/p09_sjf.py`](../code/p09_sjf.py)

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
        "bt": bt,
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

    # Shortest burst time; arrival time and input order break ties.
    selected = min(ready, key=lambda p: (p["bt"], p["at"], int(p["pid"][1:])))

    current_time += selected["bt"]
    ct = current_time
    tat = ct - selected["at"]
    wt = tat - selected["bt"]

    selected["done"] = True
    completed += 1
    total_wt += wt
    total_tat += tat
    results.append((selected["pid"], selected["at"], selected["bt"], ct, tat, wt))

print("\\nPID\\tAT\\tBT\\tCT\\tTAT\\tWT")
for row in results:
    print("\\t".join(map(str, row)))

print(f"\\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
```

## How to Run

```bash
python3 code/p09_sjf.py
```

## Result

The non-preemptive SJF scheduling algorithm was implemented and waiting time and turnaround time were calculated.

## Important Details

- This program implements **non-preemptive SJF**, not preemptive Shortest Remaining Time First (SRTF).
- Only processes that have already arrived are eligible for selection.
- If no process is ready, the CPU clock advances to the next arrival time.
- Tie-breaking is by burst time, then arrival time, then process number.
