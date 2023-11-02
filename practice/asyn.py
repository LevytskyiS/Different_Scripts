import asyncio
import time


async def get_first_data():
    start = time.time()
    ds = [i for i in range(1, 100000)]
    count = 0
    for i in ds:
        count += 1
    print(time.time() - start)
    return count


async def get_second_data():
    start = time.time()
    ds = [i for i in range(1, 110500)]
    count = 0
    for i in ds:
        count += 1
    print(time.time() - start)
    return count


async def main():
    res = await asyncio.gather(get_first_data(), get_second_data())
    return res


if __name__ == "__main__":
    asyncio.run(main())
