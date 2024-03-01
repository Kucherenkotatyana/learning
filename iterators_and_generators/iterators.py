

# ---- ---- Simple iterator ---- ----
iterable_object = [1, 2, 3]
iterator = iter(iterable_object)

print(next(iterator))


# ---- ---- Class based iterator ---- ----
class IterByList:

    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.my_list):
            raise StopIteration()
        index = self.index
        self.index += 1
        return self.my_list[index]


some_list = IterByList([1, 2, 3, 'my', 'list'])

print(next(some_list))
# returns one element or StopIteration then the list is over.


# ---- ---- Function based iterator ---- ----
def string_iterator(some_string):
    for word in some_string.split():
        yield word


test_string = "This is my test string"
iteration_string = string_iterator(test_string)

while True:
    try:
        print(iteration_string.__next__())
    except StopIteration:
        break
# returns one word each time. If StopIteration - gets out of the loop.
