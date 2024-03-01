"""
Lazy iteration.
Can iter via generator only once.
"""
import random


# ---- ---- function based generator ---- ----
def square_numbers(nums):
    for i in nums:
        yield i*i


generated_nums = square_numbers([2, 3, 4, 5])    # <generator object square_numbers at 0x7f6bd5109ca8>
print(next(generated_nums))    # 4
# returns one element or StopIteration then the list is over.

for num in generated_nums:
    print(num)    # 9 16 25


# ---- ---- generator expressions ---- ----
my_nums = (x*x for x in [2, 3, 4, 5])    # <generator object <genexpr> at 0x7f502f5dcd58>
print(list(my_nums))    # [4, 9, 16, 25]


# ---- ---- generator with random module ---- ----
def randoms_with_generator(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


rand_sequence = randoms_with_generator(1, 11, 3)
for r in rand_sequence:
    print(r)    # 3 2 5


# ---- ---- file lines generator ---- ----
def read_line_by_line(file):
    """ Lazy function (generator) to read a file line by line. """
    while True:
        line = file.readline()
        if not line:
            break
        yield line


file = open("test_text.txt")
for line in read_line_by_line(file):
    print(line.rstrip())

file.close()
