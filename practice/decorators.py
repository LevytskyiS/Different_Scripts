import time


def time_decorator(func):
    def wrapper(*args):
        start = time.time()
        func(args)
        print(args)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} seconds")

    return wrapper


@time_decorator
def func_one(num: int) -> int:
    count = 0
    for i in range(10000000):
        count += i
    return count


# func_one(10)
