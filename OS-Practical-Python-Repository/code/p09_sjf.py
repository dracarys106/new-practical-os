n = int(input("Enter number of processes: "))
if n <= 0:
    raise SystemExit("Number of processes must be positive.")

processes = []
for i in range(n):
    print(f"Process P{i + 1}")
    at = int(input("Arrival time: "))
    bt = int(input("Burst time: "))
    if at < 0 or bt <= 0:
        raise SystemExit("Arrival time must be >= 0 and burst time > 0.")
    processes.append({
        "pid": f"P{i + 1}", "at": at, "bt": bt, "done": False
    })

current_time = completed = total_wt = total_tat = 0
results = []

while completed < n:
    ready = [p for p in processes if not p["done"] and p["at"] <= current_time]
    if not ready:
        current_time = min(p["at"] for p in processes if not p["done"])
        continue

    selected = min(
        ready, key=lambda p: (p["bt"], p["at"], int(p["pid"][1:]))
    )
    current_time += selected["bt"]
    ct = current_time
    tat = ct - selected["at"]
    wt = tat - selected["bt"]
    selected["done"] = True
    completed += 1
    total_wt += wt
    total_tat += tat
    results.append((selected["pid"], selected["at"], selected["bt"], ct, tat, wt))

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for row in results:
    print("\t".join(map(str, row)))
print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
