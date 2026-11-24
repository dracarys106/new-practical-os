import os
import sys

pid = os.fork()

if pid == 0:
    print("Child: replacing child process with another Python program.", flush=True)
    os.execv(sys.executable, [sys.executable, "-c",
                              "print('Child: executing different code using exec.')"])
else:
    print("Parent: waiting for child.")
    os.waitpid(pid, 0)
    print("Parent: child has completed.")
