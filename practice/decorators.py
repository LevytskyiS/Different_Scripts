import time


def time_decorator(func):
    def wrapper(args):
        start = time.time()
        func(args)
        end = time.time()
        try:
            print(f"{func.__name__} ran in {end - start} seconds. Args: {args + 3}")
        except TypeError as e:
            print("You must pass integer. Check the argument you have passed.")

    return wrapper


@time_decorator
def func_one(num: int) -> int:
    count = 0
    for i in range(10000000):
        count += i
    return count
