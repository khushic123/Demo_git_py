from numpy import *

#Basically were just practcicng coding in python and using arrays and lists

# print fibonacci

def fib(n):
    if n < 0:
        return "Cannot print as input is invalid"

    l = [0] * n
    if n == 0:
        return l
    l[0] = 0

    if n == 1:
        return l

    l[1] = 1
    for i in range(2, n):
        l[i] = l[i - 1] + l[i - 2]
        if l[len(l) - 1] >= n:
            break;
    else:
        return l

    l.pop()

    return l


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact1(n):
    l = empty(n + 1, int)
    l[0] = 0
    l[1] = 1
    for i in range(2, n + 1):
        l[i] = i * l[i - 1]

    return l


n = int(input("Enter number:"))

ans1 = fib(n)
ans2 = fact(n)
ans3 = fact1(n)

print(ans1)
print(ans2)
print(ans3)
