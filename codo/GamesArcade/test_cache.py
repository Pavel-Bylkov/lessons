
def foo(a, b):
    return a * b + b ** 2


cache = {}


cache[(1, 2)] = foo(1, 2)
print(cache[(1, 2)])

if (2, 3) in cache:
    print(cache[(2, 3)])
else:
    cache[(2, 3)] = foo(2, 3)
    print(cache[(2, 3)])


if (2, 3) in cache:
    print(cache[(2, 3)])
else:
    cache[(2, 3)] = foo(2, 3)
    print(cache[(2, 3)])


if (1, 2) in cache:
    print(cache[(1, 2)])
else:
    cache[(1, 2)] = foo(1, 2)
    print(cache[(1, 2)])