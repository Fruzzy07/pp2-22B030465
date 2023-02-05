"""
from math import *
1-task
class Upper:
    def __init__(self):
        self.text = " "
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

write = Upper()
write.getString()
write.printString()

2-task
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

area_square = Square(10)
print(area_square.area())

3-task
class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width
area_of_rectangle = Rectangle(10,10)
print(area_of_rectangle.area())

4-task
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self,x,y):
        self.x = self.x+x
        self.y = self.y+y

    def dist(self,sum):
        dx = sum.x - self.x
        dy = sum.y - self.y
        return sqrt(dx**2 + dy**2)
coord_1 = Point(1,2)
coord_2 = Point(1,1)
print(coord_1.show())
print(coord_2.show())
coord_1.move(10,2)
print(coord_1.show())
print(coord_1.dist(coord_2))

5-task
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep_add):
        self.balance +=dep_add
        print("Deposit Accepted!")
    def withdraw(self,add):
        if self.balance >= add:
            self.balance -=add
            print("Withdrawal accepted!")
        else:
            print("Withdrawal cancelled!")

person_1 = Account("Temerlan", 0)
person_1.deposit(50)
person_1.withdraw(500)

6-task
def isPrime(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

def filter(list1):
    list2 = []
    for i in list1:
        if isPrime(i):
            list2.append(i)
    return list2

list1 = [1,2,3,4,5,6,7,8,9,10]
print(filter(list1))
"""