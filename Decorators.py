import time
from math import *


def sub(a, b):
    print("I am in original subtract function")
    return a - b


# I always want my answer to be positive but without changing the original func so will use decorator

def modified_sub(subtract):
    def modify(*args, **kwargs):
        print("Enter in modified func")
        res = subtract(*args, **kwargs)
        res = abs(res)
        print("Exit from modified func")
        return res

    return modify


a = int(input("Enter no. 1:"))
b = int(input("Enter no. 2:"))

sub = modified_sub(sub)

ans = sub(a, b)

print(ans)


# Time taken by function to execute lets say function is to calculate square

def square(n):
    print("Inside square func")
    time.sleep(0.2)
    return n * n


def calculate_time(sq):
    def wrapper(*args, **kwargs):
        begin = time.time()

        sq(*args, **kwargs)

        end = time.time()

        print("Time taken by {} func to get executes is:".format(sq.__name__), end - begin)

        return sq(*args, **kwargs)

    return wrapper


n = int(input("Enter no. to find square:"))

square = calculate_time(square)

print(square(n))
