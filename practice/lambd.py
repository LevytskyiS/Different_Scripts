import array

# res = lambda x, y: f"First num: {x}, second num: {y}"
# # print((lambda x, y: x + y)(2, 4))

# div_zero = lambda x: x / 0


# def kek(*args, **kwargs):
#     if args:
#         print(args)
#     elif kwargs:
#         print("k", kwargs)
#     else:
#         print("NONE")


# word = "hello Mike!"
# lst = [" ", "!"]

# res = len([i for i in word if i not in lst])
# print(res)

# a = [i for i in range(1, -9, -1)]
# print(a)
# N = len(a)

# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]

# print(a)

# dvojice = "Pat", "Mat"
# print(dvojice)

# arr = array.array("b", [1])
# print(arr)

a = 10

if 1 < a > 3:
    print("KEK")

a = ["L", "N", "O"]
b = [1, 2, 3]
dct = {key: value for key, value in zip(a, b)}
print(dct)
