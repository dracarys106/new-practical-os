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
