"""
1. The function compares number_to_find with the middle element.
If it matches with the middle element, we return the mid index.
2. Else if number_to_find is greater than the middle, it lies in the right (greater) half.
Else if number_to_find is smaller, it lies in the left (lower) half.
3. Then we apply the algorithm again for the chosen half.
"""


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


if __name__ == '__main__':
    numbers_list = [17, 3, 32, 11, 21, 1, 67, 90]
    number_to_find = 11

    index = binary_search(numbers_list, number_to_find)
    print(f"Number {number_to_find} is at index {index}!")
