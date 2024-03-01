"""
Bubble sort works by repeatedly replacing adjacent elements in the "bubble" until they are in the correct order.
"""


def bubble_sort(elems):
    size = len(elems)

    for i in range(size - 1):
        swapped = False
        # No swaps mean the list is already sorted, and the sorting process stops.

        for n in range(size - 1 - i):
            if elems[n] > elems[n + 1]:
                current = elems[n]
                elems[n] = elems[n + 1]
                elems[n + 1] = current
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    numbers = [21, 34, 57, 36, 11, 8, 50, 93]    # sorts by numbers
    names = ["Tetyana", "Anastasiia", "Denys", "Mary", "Olena"]    # sorts by alphabet

    bubble_sort(numbers)
    bubble_sort(names)
    print(numbers)
    print(names)
