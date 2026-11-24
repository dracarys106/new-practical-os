def allocate(blocks, processes, strategy):
    remaining = blocks[:]
    allocation = [-1] * len(processes)

    for i, process_size in enumerate(processes):
        candidates = [
            j for j, block_size in enumerate(remaining)
            if block_size >= process_size
        ]
        if not candidates:
            continue

        if strategy == "first":
            chosen = candidates[0]
        elif strategy == "best":
            chosen = min(candidates, key=lambda j: remaining[j])
        elif strategy == "worst":
            chosen = max(candidates, key=lambda j: remaining[j])
        else:
            raise ValueError("Unknown allocation strategy")

        allocation[i] = chosen
        remaining[chosen] -= process_size

    return allocation, remaining


def display(name, processes, allocation, remaining):
    print(f"\n{name}")
    print("Process\tSize\tBlock")
    for i, size in enumerate(processes):
        block = "Not allocated" if allocation[i] == -1 else f"B{allocation[i] + 1}"
        print(f"P{i + 1}\t{size}\t{block}")
    print("Remaining block sizes:", remaining)


block_count = int(input("Enter number of memory blocks: "))
if block_count <= 0:
    raise SystemExit("Number of blocks must be positive.")

blocks = []
for i in range(block_count):
    size = int(input(f"Enter size of block {i + 1}: "))
    if size <= 0:
        raise SystemExit("Block sizes must be positive.")
    blocks.append(size)

process_count = int(input("Enter number of processes: "))
if process_count < 0:
    raise SystemExit("Number of processes cannot be negative.")

processes = []
for i in range(process_count):
    size = int(input(f"Enter size of process {i + 1}: "))
    if size <= 0:
        raise SystemExit("Process sizes must be positive.")
    processes.append(size)

for strategy, title in [
    ("first", "FIRST-FIT"),
    ("best", "BEST-FIT"),
    ("worst", "WORST-FIT")
]:
    allocation, remaining = allocate(blocks, processes, strategy)
    display(title, processes, allocation, remaining)
