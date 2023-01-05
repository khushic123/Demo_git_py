from array import *
from numpy import *


def count_length_of_users(lis: array):
    s = array([], str)
    for j in lis:
        if len(j) >= 5:
            s = append(s, j)

    return s


n = int(input("Enter the no, of users:"))
List = array([], str)
for i in range(n):
    x = input("Enter the user:")
    List = append(List, x)

ans = count_length_of_users(List)
print(ans)
