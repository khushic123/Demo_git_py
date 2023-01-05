from functools import reduce

L = [1, 2, 3, 4, 5]

f = lambda l, m: l + m

a, b = 5, 5
r = f(a, b)
print(r)

p = list(filter(lambda a: a % 2 != 0, L))
print(p)

q = list(map(lambda a: a ** a, L))
print(q)

r = reduce(lambda a, b: a + b, L)
print(r)
