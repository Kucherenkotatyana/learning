import os
from contextlib import contextmanager


with os.scandir(".") as directory:
    for file in directory:
        print(file.name, "->", file.stat().st_size, "bytes")

# game_with_enum_class.py -> 1117 bytes
# setattr, getattr, hasattr, delattr.py -> 5483 bytes
# Introspection.py -> 1568 bytes
# inspect module.py -> 1125 bytes


@contextmanager
def open_file(some_file, mode):
    try:
        f = open(some_file, mode)
        yield f
    finally:
        f.close()


# Implementation:
# with open_file("text_file.txt.py", "w") as file:
#     file.write("another test string")
#
# print(file.closed)


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Implementation:
# with OpenFile("text_file.txt.py", "w") as f:
#     f.write("test string")
