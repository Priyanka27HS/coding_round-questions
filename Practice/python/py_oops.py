# 1. Inheritance

# Base class (Parent class)
class Employee:

    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee Id: {self.eid}")


# Derived class-1 <-> Child class -> Manager, Inheriting from Employee class
class Manager(Employee):

    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

    def display_info(self):
        super().display_info()
        print(f"Department: {self.dept}")


# Derived class-2 <-> Child class -> Programmer, Inheriting from Employee class
class Programmer(Employee):

    def __init__(self, name, employee_id, designation):
        super().__init__(name, employee_id)
        self.designation = designation

    def display_info(self):
        super().display_info()
        print(f"Designation : {self.designation}")


# Create instances of the classes
mngr = Manager("Ram", 17, "Analyst")
progmr = Programmer("Pavi", 127, "HR")

# Call the display_info method on instances of the classes
print("Manager Information:")
mngr.display_info()  # This will call the display_info method from the Manager class

print("Programmer Information:")
progmr.display_info()  # This will call the display_info method from the Programmer class


# using super() function example
# Base class (Parent class)
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def display_info(self):
        print(f"Color: {self.color}")


# Derived class (Child class) for Circle, inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def display_info(self):
        super().display_info()
        print(f"Shape: Circle")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area()} square units")


# Derived class (Child class) for Rectangle, inheriting from Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def display_info(self):
        super().display_info()
        print(f"Shape: Rectangle")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area()} square units")


# Create instances of the classes
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

# Call the display_info method on instances
print("Circle Information:")
circle.display_info()  # This will call the display_info method of the Circle class
print("\nRectangle Information:")
rectangle.display_info()  # This will call the display_info method of the Rectangle class


# Polymorphism using method over-riding

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Function to calculate the area of a shape
def calculate_area(shape):
    return shape.area()


# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the calculate_area function with different shapes
print(f"Circle Area: {calculate_area(circle)}")
print(f"Rectangle Area: {calculate_area(rectangle)}")

# In this example, we have a base class Shape with an area() method, and two derived classes Circle and Rectangle.
# Both derived classes override the area() method to provide their own implementations for calculating the area of
# their respective shapes. When we call the calculate_area() function with instances of these different shapes,
# polymorphism allows the correct area() method to be called based on the actual type of the object, resulting in the
# accurate calculation of the area for each shape.


# ABSTRACTION

# Define an abstract base class for BankAccount
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self, amount):
        pass


# Create a concrete class for a Savings Account
class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


# Create a concrete class for a Checking Account
class CheckingAccount(BankAccount):

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance


savings_account = SavingsAccount("AS34917", "Ram")
savings_account.deposit(17000)
savings_account.withdraw(2000)
print(f"Account Holder: {savings_account.account_holder}")
print(f"Account Balance: ${savings_account.get_balance()}")

checking_account = CheckingAccount("CA67890", "Kumar")
checking_account.deposit(33000)
checking_account.withdraw(1100)
print(f"Account Holder: {checking_account.account_holder}")
print(f"Account Balance: ${checking_account.get_balance()}")


# ENCAPSULATION
#
# which helps in hiding the internal state of an object and providing controlled access to it.
# In Python, encapsulation is achieved using private and protected attributes and methods.
# Private attributes and methods are prefixed with double underscores (__), while protected attributes and methods
# are prefixed with a single underscore (_).

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


# Creating a BankAccount object
account = BankAccount("123456", 1000)

# Accessing private attributes using public methods
print(f"Account Number: {account.get_account_number()}")
print(f"Balance: {account.get_balance()}")

# Depositing and withdrawing money
account.deposit(500)
account.withdraw(200)

# Checking the updated balance
print(f"Updated Balance: {account.get_balance()}")
