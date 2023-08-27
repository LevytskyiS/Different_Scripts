# define a list
my_list = [1, 2, 3, 4]

# create an iterator from the list
iterator = iter(my_list)

# get first object of the list
print(next(iterator))

for el in iterator:
    # выводится со второго элемента, поскольку первый был выведен ранее
    print(el)
