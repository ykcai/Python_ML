# *args and **kwargs


def myfunc(a, b):
    return sum([a, b]) * 0.05


print(myfunc(40, 60))


def myfunc2(a=0, b=0, c=0, d=0, e=0):
    return sum([a, b, c, d, e]) * 0.05


print(myfunc2(40, 60, 20))

# This isn't a very efficient solution for not passing in parameters
# Let us use *args instead

# Defintion
# *args: a function paramtere starts with an asterisk means it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values


def myfunc3(*args):
    return sum(args) * 0.05


print(myfunc3(2, 3, 5, 23, 239, 29880))


def myfunc4(*seq_of_nums):
    return sum(seq_of_nums) * 0.12


print(myfunc4(12, 343, 122, 323, 45, 2))

# Definition
# **kwargs: Python offers a way to handle arbitrary numbers of keyworded arguments. **kwards builds a dictionary of {key:value} pairs


def fruits(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}!")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


fruits(fruit='pineapple', juice="banana")


def breakfast(*args, **kwargs):
    if 'fruit' and 'juice' and 'cereal' in kwargs:
        print(
            f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"Can I get some {kwargs['cereal']}?")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


breakfast('eggs', 'bacon', 'banana', 'mouse', 'keyboard', fruit='cheeries',
          juice='lobster', cereal='fruit loops no milk')
