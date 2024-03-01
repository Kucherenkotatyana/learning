from timeit import default_timer as timer
import math
import time


""" Write a function print_check. It should display only a list of purchased goods, their quantity and cost.
Write a create_head_and_count_total dectorator. Before calling this function, it must print the header.
After calling the function print the total cost of all goods. """


def create_head_and_count_total(func):

    def wrapper(smth):
        print(">>name/count/price<<")

        func(smth)

        total_sum = 0
        for product, info in smth.items():
            total_sum += info["count"] * info["price"]
        print(f">>total sum: {total_sum}<<")

    return wrapper


@create_head_and_count_total
def print_check(some_products):

    for product, info in some_products.items():
        print(product, "-", info["count"], "x", info["price"])


check_dict = {
        "tomato": {"count": 1, "price": 25},
        "potato": {"count": 2, "price": 30},
        "lemonade": {"count": 1, "price": 15},
        "ice cream": {"count": 4, "price": 50}
    }


print_check(check_dict)

# -------------------------------------------------------------------


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'Function {func.__name__} took {end - start} for execution.')

    return inner


@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


factorial(50)
