# 1-mashq
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
# 2-mashq
class Car:
    def __str__(self):
        return "Car object"

c = Car()
print(c)
# 3-mashq
class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
# 4-mashq
class Engine:
    def start(self):
        print("Engine start")

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()
c.engine.start()
# 5-mashq
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print(self.name, self.grade)

s1 = Student("Ali", 5)
s1.info()
