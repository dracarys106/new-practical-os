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
    processes.append({"pid": f"P{i + 1}", "at": at, "bt": bt})

processes.sort(key=lambda p: p["at"])
current_time = total_wt = total_tat = 0

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    current_time = max(current_time, p["at"])
    current_time += p["bt"]
    ct = current_time
    tat = ct - p["at"]
    wt = tat - p["bt"]
    total_wt += wt
    total_tat += tat
    print(f'{p["pid"]}\t{p["at"]}\t{p["bt"]}\t{ct}\t{tat}\t{wt}')

print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
print(f"Average Turnaround Time: {total_tat / n:.2f}")
