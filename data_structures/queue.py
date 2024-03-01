"""
First in - first out.
"""

from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


my_queue = Queue()

my_queue.enqueue({
    'company': 'ATB',
    'timestamp': '23 dec, 10.09 AM',
    'price': 131.10
})
my_queue.enqueue({
    'company': 'ATB',
    'timestamp': '23 dec, 11.26 AM',
    'price': 132
})
my_queue.enqueue({
    'company': 'ATB',
    'timestamp': '23 dec, 04.10 PM',
    'price': 135
})

print(my_queue.dequeue())    # returns first object
print(my_queue.dequeue())
print(my_queue.dequeue())    # returns last object
# print(my_queue.dequeue())    # pop from an empty deque
