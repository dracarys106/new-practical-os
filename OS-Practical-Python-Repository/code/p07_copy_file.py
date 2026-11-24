import os
import sys


def copy_file(source, destination):
    source_fd = None
    destination_fd = None
    try:
        source_fd = os.open(source, os.O_RDONLY)
        destination_fd = os.open(
            destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644
        )

        while True:
            data = os.read(source_fd, 4096)
            if not data:
                break
            view = memoryview(data)
            while view:
                written = os.write(destination_fd, view)
                view = view[written:]

        print("File copied successfully.")
    finally:
        if source_fd is not None:
            os.close(source_fd)
        if destination_fd is not None:
            os.close(destination_fd)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 code/p07_copy_file.py source destination")
        sys.exit(1)
    if os.path.abspath(sys.argv[1]) == os.path.abspath(sys.argv[2]):
        print("Source and destination must be different files.")
        sys.exit(1)
    copy_file(sys.argv[1], sys.argv[2])
