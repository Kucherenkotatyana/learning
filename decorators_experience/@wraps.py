from functools import wraps


def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"Calling func {func}.")
        func(*args, **kwargs)
        print(f"Func {func} finished its work.")
    return wrap


@log_decorator
def hello():
    print("The function was called.")


hello()
