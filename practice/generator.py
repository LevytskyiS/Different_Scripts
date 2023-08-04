# генератор
gen = (i**2 for i in range(5))


# генератор с указанием yield
def f_gen(m):
    s = 1
    for n in range(1, m):
        yield n**2 + s
        s += 1


gengen = f_gen(6)
for i in gengen:
    print(i)

# генератор не хранит в себе значения в отличие от списка
