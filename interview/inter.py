import statistics
from functools import lru_cache
from collections import Counter


# Napsat funkci v pythonu, která má proměnný počet argumentů?
def func(*args):
    pass


# Napsat program, který vezme posloupnost čísel jako vstup a
# zkontroluje, zda jsou všechna čísla jedinečná
def check_unique_numbers(numbers: list) -> bool:
    if len(numbers) == set(numbers):
        return True
    return False


# Napsat program pro počítání počtu každého znaku daného textového souboru
def count_signs(text: str) -> int:
    return Counter(text)


# Provést kontrolu palindromu nad řetězcem bez použití iterační metody
def check_palindrom(word: str) -> bool:
    pal = word[::-1]
    if word == pal:
        return True
    return False


def create_triangle(base: int) -> None:
    if base % 2 == 0:
        base += 1
    space = 0

    # version 1
    for i in range(base, -1, -2):
        print(" " * space, "*" * i)
        space += 1

    # version 2
    median = statistics.median([i for i in range(1, base + 1)])
    space = median - 1
    for i in range(1, base + 1, 2):
        print(" " * space, "*" * i)
        space -= 1


@lru_cache()
def greetings(st):
    print(st)
    if len(st) == 0:
        return
    else:
        greetings(st[:-1])


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def gcd_rec(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    if min_num == 0:
        return max_num
    elif min_num == 1:
        return 1
    else:
        return gcd_rec(min_num, max_num % min_num)


class A:
    def __init__(self, name: str = "R") -> None:
        self.name = name


# Napsat program, který spustí algoritmus Bubble sort?
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list)
print("Original List: ", list)
print("Sorted List: ", sorted_list)
# a = A("K")
# a = A()
# print(a.name)
# a.__setattr__("name", "C")
# print(a.name)
# print(a.__getattribute__("name"))


lst = [12, 23, 1, 23, 5, 6, 44, 66, 88, 998, 234234234]
st = lst[0]
for i in lst:
    if st > i:
        st = i


class T:
    def __init__(self, name) -> None:
        self.name = name
