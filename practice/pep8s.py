# Hanging indent
# Correct
def long_func_name(
        var1, var2, 
        var3, var4):
    print("Kek")

foo = long_func_name(1, 2,
                     3, 4)

foo = long_func_name(
        1, 2,
        3, 4)

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()


my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


# Surround top-level function and class definitions with two blank lines.

# Method definitions inside a class are surrounded by a single blank line.

# Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

# Use blank lines in functions, sparingly, to indicate logical sections.

# Python accepts the control-L (i.e. ^L) form feed character as whitespace; many tools treat these characters as page separators, so you may use them to separate pages of related sections of your file. Note, some editors and web-based code viewers may not recognize control-L as a form feed and will show another glyph in its place.

# Correct:
import os
import sys

# Correct:
from subprocess import Popen, PIPE

# Imports should be grouped in the following order:
# Standard library imports.
# Related third party imports.
# Local application/library specific imports.
# You should put a blank line between each group of imports.

# Correct:
spam(ham[1], {eggs: 2})

# Correct:
foo = (0,)

# Correct:
if x == 4: print(x, y); x, y = y, x

# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Correct:
spam(1)

# Correct:
dct['key'] = lst[index]

# Correct:
x = 1
y = 2
long_variable = 3

# If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). 
# Use your own judgment; however, never use more than one space, 
# and always have the same amount of whitespace on both sides of a binary operator:
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# When combining an argument annotation with a default value, however, do use spaces around the = sign:
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# While sometimes it’s okay to put an if/for/while with a small body on the same line, 
# never do this for multi-clause statements. Also avoid folding such long lines!

# Trailing commas
# Correct:
FILES = ('setup.cfg',)

# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# Docstrings
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
# OR
"""Return an ex-parrot."""