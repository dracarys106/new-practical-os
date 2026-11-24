def read_meminfo():
    memory = {}
    with open("/proc/meminfo", "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.split(":", 1)
            parts = value.strip().split()
            if parts and parts[0].isdigit():
                memory[key] = int(parts[0]) * 1024
    return memory


def to_mb(byte_value):
    return byte_value / (1024 * 1024)


try:
    mem = read_meminfo()
    total = mem.get("MemTotal", 0)
    free = mem.get("MemFree", 0)
    available = mem.get("MemAvailable", free)
    used = total - available

    print("LINUX MEMORY INFORMATION")
    print("------------------------")
    print(f"Configured / Total memory : {to_mb(total):.2f} MB")
    print(f"Free memory               : {to_mb(free):.2f} MB")
    print(f"Available memory          : {to_mb(available):.2f} MB")
    print(f"Estimated used memory     : {to_mb(used):.2f} MB")
except (OSError, ValueError) as error:
    print("Unable to read memory information:", error)
