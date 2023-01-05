# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# now we are required to tell Python
# for 'Main' function existence

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


a = '11001'
b = a[::-1]
print(b)

ans = 0;
for i, j in zip(range(len(b)), b):
    ans = ans + 2 ** i * int(j)

print(ans)

x, y = 2, 3
x, y = y, x

print(x, y)

t = []
n = [1, 2, 3]
t.append(n)
print(t)
vis = [False] * len(n)
print(vis)

from numpy import *

v1 = array([1, 2, 3])
v2 = array([4, 5, 6])

v3 = empty((0,1),int)
i, j = 0, 0
while i < len(v1) and j < len(v2):
    a=v1[i]+v2[j]
    v3=append(v3,a)
    i += 1
    j += 1

print(v3)
m1 = array([
    [1, 2, 3],
    [6, 4, 5],
    [1, 6, 7],
])
m2 = array([
    [1, 2, 3],
    [6, 8, 5],
    [2, 6, 7],
])

a = m1.shape
b = m2.shape
ans = empty((0,3),int)

r1, c1 = a[0], a[1]
r2, c2 = b[0], b[1]

for i in range(r1):
    L = empty((0,1),int)
    for j in range(c2):
        z = 0
        p, t = 0, 0
        while p < c1 and t < r2:
            z = z + m1[i][p] * m2[t][j]
            p += 1
            t += 1

        L=append(L,z)

    ans=append(ans,[L],axis=0)

print(ans)
m3=matrix(ans)
print(m3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
