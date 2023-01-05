class College:
    # class or static variables:
    clg_name = "LNMIIT"
    Fees = 2000000

    def __init__(self, name, roll, branch):
        # instance variables
        self.name = name
        self.roll = roll
        self.branch = branch

    def instance_method(self):
        self.name = "tithi"
        return self.name

    @classmethod
    def class_method(cls):
        return cls.clg_name, cls.Fees

    @staticmethod
    def static_method():
        return "Hey I neither deal with instance nor class/static variables"


s1 = College("Khushi", "19ucc141", "cce")
s2 = College("Karan", "19ucc025", "cse")

a = s1.instance_method()
b = College.class_method()
c = College.static_method()
print(a, b, c)

print(s2.name, s2.roll, s2.branch, College.clg_name, College.Fees)


# INNER CLASSES

class Student:

    def __init__(self, name, roll, brand, ram):
        self.name = name
        self.roll = roll
        # creating object of class laptop inside outer class
        self.laptop = self.Laptop(f"{brand}", f"{ram}")

    def show(self):
        print(self.name, self.roll)
        print(self.laptop.show())

    class Laptop:

        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram

        def show(self):
            return self.brand, self.ram


# what if khushi has 2 laptops
s1 = Student("khushi", "19ucc141", "MAC", "8GB")
s1.show()


# s11= Student.Laptop("mac","8gb")
# print(s11.show())


# OPERATOR OVERLOADING

class CollegeStudent:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s = CollegeStudent(m1, m2)
        return s

    def __gt__(self, other):
        m1 = self.m1+self.m2
        m2 = other.m1+other.m2
        if m1 > m2:
            return True
        else:
            return False


s1 = CollegeStudent(10, 20)
s2 = CollegeStudent(30, 40)

# CollegeStudent.__add__(s1,s2)
s3 = s1 + s2
print(s3.m1, s3.m2)

#College.Student.gt(s1,s2)
if s1 > s2:
    print("s1 is intelligent then s2")
else:
    print("s2 is intelligent then s1")


