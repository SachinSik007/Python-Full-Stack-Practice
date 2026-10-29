# 1. What is OOP? What are its advantages?
# **OOP stands for Object-Oriented Programming. It is a programming approach based on classes and objects. 
# It helps us organize code, reuse functionality, and maintain applications easily.

# Real-life example: A car has properties like color, model, and speed, and behaviors like start, stop, and accelerate.
# class Car:
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model

#     def start(self):
#         print(f"{self.model} is starting")

# car1 = Car("Black","Swift")
# car1.start()

# 2. What is the difference between a class and an object?
# class - A class is a blueprint used to create objects
# object - An object is an instance of a class that contains its own data and can use the class's methods.

# Real-life example: A house blueprint is a class, and the actual houses built from that blueprint are objects.

# class Student: # class
#     def __init__(self,name):
#         self.name = name

#     def study(self):
#         print(f'{self.name} is studying')

# student1 = Student("Rahul") # object
# student2 = Student("Mohit")

# student1.study()
# student2.study()

# 3. What is the purpose of the __init__() method?
#  The __init__() method is an initializer that runs automatically after an object is created. 
# It is commonly used to initialize an object's attributes.

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance

# account = BankAccount("Sachin",2500)
# print(account.name)
# print(account.balance)

# 4. What is self in Python?
# self refers to the current instance of a class. 
# We use it to access that object's attributes and instance methods. 
# It is a naming convention, not a Python keyword.

# class Student:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course

#     def display(self):
#         print(f'{self.name} : {self.course}')

# s1 = Student("Radhe","MCA")
# s2 = Student("Mohit","BCA")
# s1.display()
# s2.display()

# 5. What are the four pillars of OOP?
# The four pillars of OOPs are encapsulation, 
# inheritance, polymorphism, and abstraction.

# 1. Encapsulation

# Bundles data and methods together and controls access to data.

# Example: A bank account protects its balance from unauthorized changes.

# 2. Inheritance

# Allows one class to reuse features of another class.

# Example: A child inherits certain characteristics from their parents.

# 3. Polymorphism

# The same interface or method name can have different behaviors.

# Example: Cars, buses, and bikes all have a start() operation, but the implementation may differ.

# 4. Abstraction

# Hides implementation details and exposes essential operations.

# Example: You withdraw cash from an ATM without knowing its internal processing.

# 6. What is inheritance? Explain its different types in Python.
# Answer: Inheritance allows a child class to reuse attributes and methods
#  from a parent class. It reduces code duplication.

# Real-life example: A Manager is an employee, so the Manager class can inherit common employee features.

# class Employee:
#     def work(self):
#         print("Employee is Working")

# class Manager(Employee):
#     def manage_team(self):
#         print("Manager of the Team")

# manager = Manager()
# manager.work()
# manager.manage_team()

# ***********************Types of Inheritence******************
# 1. Single inheritance ?
# One child inherits from one parent.
# Animal → Dog

# 2. Multiple inheritance ?
# One child inherits from multiple parents.
# Father + Mother → Child 

# 3. Multilevel inheritance
# A class inherits from a child class, creating a chain.
# Animal → Dog → Puppy

# 4. Hierarchical inheritance
# Multiple child classes inherit from one parent.
# Animal → Dog, Cat

# 5. Hybrid inheritance
# A combination of two or more inheritance types.

# 7. What is multiple inheritance?
# Multiple inheritance occurs when a single child class inherits from two or more parent classes.

# Real-life example: A smart device can have both camera functionality and music-player functionality.

# class Camera:
#     def take_photo(self):
#         print("Click the photo")

# class MusicPlayer(Camera):
#     def play_list(self):
#         print("Playing Music")

# class SmartPhone(MusicPlayer):
#     def smart_phone(self):
#         print("SmartPhone Take a Features")

# s1 = SmartPhone()
# s1.take_photo()
# s1.play_list()
# s1.smart_phone()

# 8. What is method overriding? Give an example.
# Method overriding occurs when a child class provides 
# its own implementation of a method already defined in its parent class.

# class Employee:
#     def work(self):
#         print("Employee performs general works")

# class Developer(Employee):
#     def work(self):
#         print("Developer Writes the code")

# c1 = Developer()
# c1.work()

# 9. Does Python support method overloading? How can you achieve similar behavior?
# Python does not support traditional method overloading by defining multiple methods with the same name and 
# different parameter lists in the way languages like Java do. A later definition normally replaces an earlier one.

# We can achieve similar behavior using default arguments, *args, or functools.singledispatch for type-based function dispatch.

# class Calculator:
#     def add(self,a,b=0,c=0):
#         return a + b + c

# calc = Calculator()
# print(calc.add(10,20))
# print(calc.add(10,20,30))
# print(calc.add(10))

# 10. What is polymorphism?
# Answer: Polymorphism means "many forms." It allows the same method name or 
# interface to work with different types of objects.
# Real-life example: Different payment methods perform the same pay() operation differently.

# class UPI:
#     def pay(self):
#         print("Payment Throught Successfully")

# class Card:
#     def pay(self):
#         print("Payment Through Success")

# class Cash:
#     def pay(self):
#         print("Payment Through Cash")

# def make_payment(payment_method):
#     payment_method.pay()

# make_payment(UPI())
# make_payment(Cash())
# make_payment(Card())

# 11. What is encapsulation?
# Answer: Encapsulation means bundling data and the methods that operate
# on it inside a class, while controlling how that data is accessed or modified.

# Real-life example: In a bank account, a user should not directly set 
# the balance to an arbitrary amount. Deposits and withdrawals should follow rules.

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())

# 12. Does Python support private and protected members? Explain naming conventions.
# Python does not enforce access modifiers like Java. It uses naming conventions and name mangling to communicate intended access.
# Naming	                      Meaning	         Example
# name	                           Public	           self.name
# _name	                      Protected by convention	self._salary
# __name	                     Name-mangled	       self.__balance

# class Employee:
#     def __init__(self):
#         self.name = "Rahul"
#         self._dept = "IT"
#         self.__salary = 2300

# e = Employee()
# print(e.name)
# print(e.__salary)
# print(e._dept)

# 13. What is abstraction? How does the abc module help?
# Abstraction hides implementation details and exposes only the essential functionality. Python provides the abc module to define abstract base classes and abstract methods.
# An abstract class cannot be instantiated while it still has unimplemented abstract methods.
# Real-life example: A payment system requires every payment method to implement pay(), but each method can process the payment differently.

# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class UPIPay(Payment):
#     def pay(self,amount):
#         print(f'Paid : {amount} using UPI')

# s = UPIPay()
# s.pay(500)

# 54. What is the difference between an instance method, class method, and static method?
# Answer: Python provides three common method types.
# Method	            First parameter	                Used for
# Instance               method	self	           Accessing or modifying object-specific data
# Class method	            cls	                       Accessing or modifying class-level data
# Static method	     No automatic first parameter	Related utility logic

# class Student:
#     school = "Dauji Public School"

#     def __init__(self,name):
#         self.name = name

#     #instance method
#     def show_data(self):
#         return self.name

#     @classmethod
#     def show_school(cls):
#         return cls.school

#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# e = Student("Rahul")
# print(e.show_data())
# print(e.show_school())
# print(e.is_adult(23))

# 55. What is the difference between a class variable and an instance variable?
# A class variable is shared through the class, while an instance variable 
# stores data specific to an object.

# Real-life example: Employees work for the same company, but each employee has a different name.

# class Employee:
#     company = "Faithcode Technologies" # class Variable

#     def __init__(self,name):
#         self.name = name # instance varibale

# s2 = Employee("Mohit")
# print(s2.name)
# print(s2.company)

# 16. What is super() and when do you use it?
# super() provides access to methods in the next class in the Method Resolution Order. 
# It is commonly used to call parent-class implementations, especially in constructors.

# Real-life example: A manager is an employee, so the manager's initialization can reuse the '
# 'employee's initialization.

# class Student:
#     def __init__(self,name):
#         self.name = name

# class Teacher(Student):
#     def __init__(self, name,team_size):
#         super().__init__(name)
#         self.team_size = team_size

# t = Teacher("Rahul",5)
# print(t.name)
# print(t.team_size)

# 17. What is MRO (Method Resolution Order)?
# MRO stands for Method Resolution Order. It defines the order Python follows 
# when searching for a method or attribute in a class hierarchy, particularly with multiple inheritance.
# Python uses the C3 linearization algorithm to determine this order.

# Real-life example: If a smart device inherits from two classes that both define the same method, MRO determines which method is found first.

# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")

# class C(B):
#     def show(self):
#         print("Class C")

# class D(B,C):
#     pass

# obj = D()
# obj.show()

# print(D.mro())

# 58. What are @property, getter, and setter methods?
# @property allows a method to be accessed like an attribute. 
# A getter retrieves a value, while a setter validates or controls how a value is updated.

# Real-life example: An employee's salary should not be negative, so we validate it before accepting an update.

# class Employee:
#     def __init__(self,salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self,value):
#         if value < 0:
#             raise ValueError("Salary can not be negative")
#         self._salary = value

# e = Employee(30000)
# print(e.salary)
# e.salary = 40000
# print(e.salary)

# 19. What is composition, and how is it different from inheritance?
# Composition means building a class by including objects of other classes. 
# Inheritance represents an "is-a" relationship, while composition commonly represents a "has-a" relationship.

# Real-life example: A car has an engine, but a car is not an engine.

# class Engine:
#     def start(self):
#         print("Engine Started")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def start_car(self):
#         self.engine.start()
#         print("Car Start")

# car = Car()
# car.start_car()


############################## Task ##############################

# Q - How would you design a simple Employee or BankAccount class using OOP principles?
# Ans - I would create a class containing attributes and methods. I would use encapsulation to control
# access to sensitive data, validation to prevent invalid operations, and clear methods to expose the required functionality.

# Real-life example: Bank account system

class BankAccount:
    def __init__(self,accoun_holder,balance = 0):
        self.account_holder = accoun_holder
        self.__balance = balance

        if balance < 0:
            raise ValueError("Balance can not be Negative")

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")

        self.__balance += amount
        print(f'Deposited : {amount}')

    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("Withdrawl must be positive")

        if amount > self.__balance:
            print("Insufficient Balance")
            return
        self.__balance -= amount
        print(f'Withdral : {amount}')

    def get_balance(self):
        return self.__balance

account = BankAccount("Rahul",5000)
account.deposit(2000)
account.withdraw(3500)

print(f'Account Holder : {account.account_holder}')
print(f'Balance : {account.get_balance()}')