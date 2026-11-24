import os
import platform

print("LINUX KERNEL AND CPU INFORMATION")
print("--------------------------------")
print("Operating system:", platform.system())
print("Kernel release:", platform.release())
print("Kernel version:", platform.version())
print("Machine architecture:", platform.machine())
print("Processor:", platform.processor() or "Not reported by platform module")
print("Logical CPU count:", os.cpu_count())

try:
    with open("/proc/cpuinfo", "r", encoding="utf-8") as file:
        cpu_info = file.read()
    print("\nDetailed CPU information (first processor entry):")
    print(cpu_info.split("\n\n")[0])
except OSError as error:
    print("Could not read /proc/cpuinfo:", error)
