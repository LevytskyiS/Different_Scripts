import time

from numba import njit, prange


@njit(fastmath=True)
def get_res():
    r = []
    for i in prange(10000000000):
        r.append(i**2 / 0.123)
    return sum(r)


start = time.perf_counter()
print(get_res())
end = time.perf_counter()
print(end - start)
