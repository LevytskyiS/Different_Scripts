# 1.Vysvětlete programovací jazyk Python?
# 2. Seznam výhod pythonu?
# 3. Proč je python dynamicky typovaný jazyk?
# 4. Vysvětlete „Python je interpretovaný jazyk“?
"""
Python is an interpreted language, 
which means the source code of a Python program is converted into bytecode 
that is then executed by the Python virtual machine. 
Python is different from major compiled languages, such as C and C + +, 
as Python code is not required to be built and linked like code for these languages.
"""
# 5. Víte o PEP 8 a proč je důležitý?
# 6. Vysvětlete rozsah v pythonu?
""" 
The range() function in Python is used to generate a sequence of 
numbers within a specified range.

PYTHON 2
Range returns an iterator that is memory-efficient for large ranges 
because it generates values on the fly.  
"""
# 7. Definovat seznamy a n-tice?
# 8. Vysvětlete klíčový rozdíl mezi seznamem a n-ticemi?
# 9. Pojmenujte běžné vestavěné datové typy v pythonu?
# 10. Co je pass v Pythonu?
""" 
The pass statement in Python is a placeholder statement that does nothing. It is used as a
syntactic placeholder when a statement is required by the Python syntax, but no action is
needed.
"""
# 11. Co jsou balíčky a moduly v pythonu?
# 12. Vysvětlit globální, chráněné a soukromé atributy v Pythonu?
""" 
A global variable in Python means having a scope throughout the program, i.e., 
a global variable value is accessible throughout the program unless shadowed.  
"""
# 13. Zdůraznit použití sebe sama v Pythonu?
""" 
Recursion is a process in which a function calls itself directly or indirectly. 
"""
# 14. Co v tom je"?
# 15. Vysvětlete přerušení, pokračování a předání v pythonu?
"""Break, continue, pass or return?"""
# 16. Co jsou unit testy v pythonu?
# 17. Co je docstring v Pythonu?
""" 
A docstring is a string literal that occurs as the first statement in a module, function, 
class, or method definition. The docstring is a phrase ending in a period. 
It prescribes the function or method’s effect as a command (“Do this”, “Return that”), 
not as a description; e.g. don’t write “Returns the pathname …”.
"""
# 18. Co je krájení v pythonu?
""" 
Slicing in Python is a feature that allows you to retrieve or modify subsets of sequences, 
such as lists or strings. Sequences can be sliced using the scheme 
[start:stop:step], where 'start' is the index where the slice starts, 
'stop' is the index where the slice ends, and 'step' is the difference between each index.
"""
# 19. Napište syntaxi, aby byl skript Python spustitelný na Unixu?
"""#!/usr/bin/env python3 - must occur as the first statement"""
# 20. Jaký je klíčový rozdíl mezi Python Arrays a seznamy?
""" 
List - Can consist of elements belonging to different data types
Array - Only consists of elements belonging to the same data type
"""
# 21. Je python jazykem rozlišujícím velká a malá písmena?
# 22. Jak dlouho bude identifikátor v Pythonu?
""" 
id() function in python is used to find the memory address referenced by a variable
Identifikátor x existuje pouze tehdy, když má nějakou hodnotu. 
Neexistuje mezi nastavením x na None a znovu ho nastavením na 20.
"""
# 22. Jak převedete řetězec na malá písmena?
# 23. Vysvětlete jmenné prostory Pythonu a jejich použití?
""" 
Variable scope means the area in which parts of a program can access the variable. 
There are four variable scopes in python:

Local
Global
Enclosing
Built-in
"""
# 24. Co je rozlišení rozsahu v Pythonu?
# 25. Co jsou dekoratéři v Pythonu?
"""
A decorator in Python is a design pattern that allows a user to add new functionality 
to an existing object without modifying its structure.
"""
# 26. Definovat lambda v Pythonu? Jaké má využití?
""" 
A lambda function is an anonymous function in Python that is defined using the lambda
keyword. It is a shorthand way to create small, one-line functions without explicitly 
defining a function using def.
"""
# 27. Zvýrazněte rozdíl mezi xrange a range v Pythonu?
# 29. Definovat odmořování a moření v pyhtonu?
""" 
The pickle module in Python provides functions for serializing and deserializing Python
objects. It allows you to convert Python objects into a binary format that can be stored or
transmitted, and then restore them back into objects.
"""
# 30. Co jsou generátory v Pythonu?
""" 
A generator in Python is a type of iterable that produces a sequence of results 
instead of storing them in memory. Unlike a list or a tuple, the elements of a generator 
are created on the fly as they are needed. This feature allows for efficient and 
flexible data processing, especially when dealing with large datasets.

g = (x**2 for x in range(5)) - Generator expression
def squares(n): - Generator function
    for x in range(n):
        yield x**2
"""
# 31. Vysvětlete, jak jsou argumenty předávány hodnotou a předávány odkazem v pythonu?
# 32. Co jsou iterátory v Pythonu?
""" 
An iterable object is an object that implements __iter__, which is expected to 
return an iterator object."

"An iterator object implements __next__, which is expected to return the next element of 
the iterable object that returned it, and to raise a StopIteration exception when no 
more elements are available.
"""
# 33. Jak smazat soubor v Pythonu?
""" os.remove() """
# 34. Jak odstranit duplicitní prvek ze seznamu v pythonu?
""" set() """
# 35. Vysvětlete účel bytes() v Pythonu?
"""
The main purpose of the bytes() method in Python is to convert an object or sequence 
of objects to a bytes object. This method allows us working with binary data and 
handling bytes data from a buffer.

# convert a string to bytes
string = "Hello, World!"
bytes_object = bytes(string, encoding='utf-8')
print(bytes_object) # b'Hello, World!'
"""
# 36. Jak vytvoříte třídu v Pythonu?
""" It's needed to use the 'class' keyword nad a name of a new class."""
# 37. Vysvětlete koncept dědičnosti v Pythonu na příkladu?
"""
"In Python it is possible to create an object that inherits the methods and properties 
of another object. This is called inheritance. In inheritance, there is a parent class 
and a child class. A child class inherits the properties and methods of the parent class."
"""
# 38. Jak získáte přístup k rodičům v dětské třídě v Pythonu?
""" class Child(Parents) """
# 39. Využívá Python specifikátory Accessu?
""" Yes, Python uses accessor specifications to control how attributes can be accessed."""
# 40. Je možné zavolat nadřazenou třídu bez vytvoření její třídy?
""" No """
# 41. Jak vytvoříte prázdnou třídu v pythonu?
""" 
class A:
    pass
"""
# 42. Zmínit klíčový rozdíl mezi novými a přepsanými modifikátory?
# 43. Proč v Pythonu používáme metodu finalizace?
# 44. Vysvětlete metodu 'init' v Pythonu?
"""
The python __init__ method is declared within a class and is used to initialize
the attributes of an object as soon as the object is formed.
"""
# 45. Pojmenujte metodu použitou ke kontrole, zda je třída potomkem jiné třídy?
""" issubclass() """
# 46. Rozdíl mezi modulem a balíčkem v pythonu?
""" 
In summary, a package is a collection of related modules, while a module is
a single python file that contains a set of related functions, classes, 
and global variables.
"""
# 47. Jmenujte nejčastěji používané vestavěné moduly v Pythonu?
"""
Sys, os, math, random, re, time, json
"""
# 48. Vysvětlete funkce lambda?
# 49. Jak generovat náhodná čísla v Pythonu?
""" Using the random module """
# 50. Je možné zkontrolovat, zda jsou všechny znaky v daném řetězci alfanumerické?
""" isalnum() """
# 51. Definovat Global Interpreter Lock?
""" 
The Global Interpreter Lock (GIL) is a mutex that prevents multiple native threads 
from executing Python bytecodes at once. This lock is necessary because CPython's 
memory management is not thread-safe.

Although the GIL is present, Python is still able to perform other operations concurrently, 
such as I/O and networking, thanks to its event-driven architecture and 
libraries like asyncio.
"""
# 52. Definovat Pythonpath?
"""
The PYTHONPATH environment variable is a list of directories that Python uses to search 
for modules and packages.

The sys.path list contains the directory names that Python searches for modules. 
This list is initially populated from the PYTHONPATH environment variable, 
the PYTHONHOME environment variable, and the installation-dependent default path.
"""
# 53. Definovat PIP?
"""
PIP, which stands for "Pip Installs Packages," is the package installer for Python. 
It is used to install and manage software packages written in Python.
"""
# 54. Je v pythonu k dispozici nějaký nástroj pro identifikaci chyb?
# 55. Pojmenujte nástroj používaný k provádění statické analýzy v pythonu?
""" pylint package """
# 56. Rozdíl mezi hlubokými a mělkými kopiemi?
"""
The copy() method only creates a shallow copy of the original object. 
It copies the reference of the original object to the new object. So, 
any changes made to the new object will also reflect in the original object 
because both are pointing to the same memory location.

On the other hand, the deepcopy() method creates a deep copy of the original object. 
It doesn't copy the reference of the original object but creates
a new object with the same values as the original object. So, 
any changes made to the new object won't reflect in the original object
because they are two different objects with two different memory locations.
"""
# 57. Jaká je hlavní funkce v pythonu?
""" main() """
# 58. Jak vyvolat hlavní funkci v pythonu?
"""
To run a python program from the command line, you need to call the main function 
using the -m flag followed by the module name.

python -m myscript (without the .py suffix)
"""
# 59. Function
"""
A function is a block of organized and reusable code that performs a single-related
action or operation.
"""
# 60. Flask & Django
"""
Philosophy:

Flask is a micro-framework, meaning it provides minimal functionality. 
Flask does not have an ORM (Object Relational Mapper) built in. This allows 
the developer more freedom in choosing their own tools.

Django is a full-stack framework. Django has everything you need to start 
a web application. Django's ORM, Admin Interface, and authentication system 
are included out of the box.

Project Structure:

Flask projects tend to be smaller and less complex, with less code needed for
the same functionality. This is because Flask provides fewer abstractions.

Django projects are usually larger and more complex, as Django includes a 
lot of functionality out of the box.

Community and Ecosystem:

Django has a larger and more established community. This means Django has more 
third-party packages, libraries, and plugins available.

Flask's community is smaller, but growing. The smaller community also means 
less pre-built functionality available, but also potentially more flexibility.

Learning Curve:

Django has a steeper learning curve, as it has a lot more features out of the box.
Flask has a gentler learning curve, as it requires less setup and less 
configuration.

Debugging:

Flask comes with Werkzeug, a powerful debugging tool. 
Werkzeug helps developers identify issues and errors more easily.

Django also includes a built-in debugger called pdb.

In summary, Flask is a good choice if you want more control and 
a more minimalistic approach to web development. On the other hand, 
Django is a better choice if you want a more full-featured web framework 
that offers more out of the box.
"""

import sys
import copy
import os

word = "HELLO!"
print(word.lower())

set1 = {1, 2, 3}
print(type(set1))
# set2 = {1, 2, [3]}
# print(type(set2))

l = [1, 2, 3, [4, 5]]
res = []


def recursion_func(arr: list):
    for el in arr:
        if isinstance(el, int):
            res.append(el)
        else:
            recursion_func(el)


n = 10
c = 10
# print(id(n), "; ", id(c))
# for i in range(n):
#     if i < 3:
#         print("pass")
#         pass
#     elif 3 <= i < 6:
#         print("cont")
#         continue
#     else:
#         print("ret")

print(sys.path)

a = [1, 2, [3, 4]]
b = [1, 2, [3, 4]]
c = copy.copy(a)
c[2].append(5)
d = copy.deepcopy(b)
d[2].append(5)
print(a, c, " : ", b, d)

f = "ts.py"
try:
    os.remove(f)
except FileNotFoundError as e:
    print("File not found")
