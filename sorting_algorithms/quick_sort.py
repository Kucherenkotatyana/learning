

def partition(array, start, end):
    # choose the rightmost element as pivot
    pivot = array[end]

    # pointer for greater element
    i = start - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(start, end):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[end]) = (array[end], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


numbers_list = [17, 3, 32, 11, 21, 1, 67, 90]
size = len(numbers_list)

quicksort(numbers_list, 0, size - 1)

print(f"Sorted Array in Ascending Order:\n{numbers_list}")
