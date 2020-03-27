import this


def func(a, b=None, c=None):
    if b is None:
        b = [1, 2, 3]
    if c is None:
        c = {'Rahul': 'Jha'}
    print(a, b, c)
