
def BinarySearch(num ,l ,r ,x):
    while l<= r:
        m = l + (r - l) // 2
        if num[m] == x:
            return True, m

        if num[m] < x:
            return BinarySearch(num, m + 1, r, x)
        elif num[m] > x:
            return BinarySearch(num, l, m - 1, x)

    return False


n = int(input("Size of list: "))
num = [0] * n

for i in range(n):
    a = int(input("Enter the number in List:"))
    num[i] = a

print(num)

x = int(input("Enter the number you want to search for:"))

num.sort()

print(BinarySearch(num, 0, n - 1, x))

for i in range(5,0,-1):
    print(i)