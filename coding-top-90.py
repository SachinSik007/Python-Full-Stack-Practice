# 1. Reverse a string without using slicing or reversed().
# s = "programming"
# rev = ''
# for char in s:
#     rev = char + rev

# print(rev)

# 2. Check whether a string is a palindrome.
# numbers = int(input("Please Enter Your Number : "))
# temp = numbers
# rev = 0

# while numbers > 0:
#     digit = numbers % 10
#     rev = rev*10 + digit
#     numbers = numbers//10

# if rev == temp:
#     print(f'{temp} is a Palindorme')
# else:
#     print("Not Palindrome")

# 3. Find the largest and second-largest numbers in a list.

# numbers = [10,40,50,70,20,30,90]

# first = second = float("-inf")

# for num in numbers:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num

# print(f'{second} is Second Highest')
# print(f'{first} is  Highest')

# 4. Count the frequency of each character in a string.

# s = "pythonprogramminqqqqwwe2333223@@"
# count = {}

# for char in s:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# print(count)

# 5. Remove duplicate elements from a list while preserving order.

# numbers = [10,20,30,20,30,50]
# duplicate = []

# for num in numbers:
#     if num not in duplicate:
#         duplicate.append(num)

# print(duplicate)

# 6.Count vowels and consonants in a string.

# s = "programming"
# vowel = 0
# consonent = 0

# for char in s:
#     if char not in "aeiou":
#         vowel += 1
#     else:
#         consonent += 1

# print(vowel)
# print(consonent)

#7. Check whether a number is prime.

# numbers = int(input("Please Enter Your Number : "))
# num = 0

# if numbers <= 1:
#     print("Not a prime")
# else:
#     for i in range(2,numbers):
#         if numbers % i == 0:
#             num = 1
#             break

#     if num == 0:
#         print(f'{numbers} is a Prime')
#     else:
#         print("Not Prime Number")


# 8. Generate the Fibonacci sequence for n terms.

# def fabanicci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fabanicci(n-1) + fabanicci(n-2)

# n = 5
# for i in range(n):
#     print(i, end=" ")


# 9. Find the common elements between two lists without duplicates in the result.

# list1 = [1,2,3,4]
# list2 = [1,2,3]

# common = []

# for sublist in list1:
#     if sublist in list2:
#         common.append(sublist)

# print(common)

# 10. Sort a list of dictionaries by a specific key, such as age.

# people = [
#     {"name": "Amit", "age": 25},
#     {"name": "Ravi", "age": 20},
#     {"name": "Priya", "age": 30},
#     {"name": "Neha", "age": 22}
# ]

# sorted_people = sorted(people, key = lambda x:x["age"])
# print(sorted_people)

#11. Check whether two strings are anagrams.
# str1 = "silent"
# str2 = "listen"

# if len(str1) != len(str2):
#     print("Not Args")

# else:
#     for char in str1:
#         if str1.count(char) != str2.count(char):
#             print("not Args")
#             break
#     else:
#         print("Args")

# 12. Find all duplicate elements in a list.
# numbers = [10,20,10,20,30,40]
# duplicates  = []
# seen = []

# for num in numbers:
#     if num in seen:
#         if num not in duplicates:     
#            duplicates.append(num)
#     else:
#         seen.append(num)

# print(duplicates)

# 13.Flatten a nested list one level deep.
# lists = [[1,2],[3,4],[5,6]]
# nested_list = []

# for num in lists:
#     for num2 in num:
#         nested_list.append(num2)

# print(nested_list)

# 14. Find the missing number in a list containing numbers from 1 to n, with one number missing.

# numbers = [1,2,3,5]
# n = 5

# for num in range(1,n+1):
#     if num not in numbers:
#         print("Missing NUmber is : ",num)
#         break

# 15. Group a list of words by their first character using a dictionary.

# words = ["apple", "ant", "banana", "ball", "cat", "car"]
# group = {}

# for word in words:
#     first = word[0]

#     if first not in group:
#         group[first] = []

#     group[first].append(word)

# print(group)

#16. Write a generator that yields even numbers from 1 to n.

# def genrator(n):
#     for num in range(1,n+1):
#         if num % 2 == 0:
#             yield num

# gen = genrator(10)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 17. Create a decorator that prints a function's name before executing it.
# def decorator(func):
#     def wrapper():
#         print("Function name:", func.__name__)
#         result = func() + 15
#         print("after Exceution")
#         return result
#     return wrapper

# @decorator
# def add():
#     a = 10
#     b = 20
#     return a + b

# print(add())


# 18.Create a decorator that measures a function's execution time.

# import time

# def decorator(func):
#     def wrapper():
#         start = time.time()

#         result = func()

#         end = time.time()

#         print("Execution time:", end - start, "seconds")
#         return result

#     return wrapper

# @decorator
# def calculation():
#     total = 0
#     for i in range(1000000):
#         total += i
#     return total

# print(calculation())

# 19. Implement a custom iterator that returns numbers from 1 to n.

# def cust_genrator(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# for num in cust_genrator(5):
#     print(num)

# 20. Write a function that accepts any number of positional and keyword arguments using *args and **kwargs.

# def my_function(*args,**kwargs):
#     print("Positional Arguments",args)
#     print("Keyword Arguments",kwargs)

# my_function(10,20,30,name="Sachin",age=20)

# 21. Write a context manager that measures how long a block of code takes.

# from contextlib import contextmanager

# import time

# @contextmanager
# def timer():
#     start = time.time()
#     try:
#         yield
#     finally:
#         end = time.time()
#         print(f'Execution Time : {end - start:.4f} seconds')

# with timer():
#     time.sleep(2)

# 22.Use map(), filter(), and a lambda function to transform and filter a list of numbers.

# from functools import reduce

# numbers = [1,2,3,4,5]
# result = list(map(lambda x : x**2,numbers))
# print(result)

# result2 = list(filter(lambda x:x%2==0,numbers))
# print(result2)

# result3 = reduce(lambda x,y:x+y,numbers)
# print(result3)

# 23. Demonstrate shallow copy versus deep copy using a nested list.

# import copy 

# original = [[1,2],[3,4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0][0] = 99
# print(shallow)
# print(deep)

# 24. Write a function that safely handles division by zero and invalid numeric input using exception handling.

# def safe_division(a,b):
#     try:
#         a = float(a)
#         b = float(b)
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Errro : Can not divided by zero"
#     except ValueError:
#         return "Error : Invalid Numeric Value"

# print(safe_division(10,2))
# print(safe_division(10,0))
# print(safe_division("abc",2))

# 25. Create a Student class with name, age, and marks attributes and a method to display student details.

# class Student:
#     def __init__(self,name,age,marks):
#         self.name =  name
#         self.age =  age
#         self.marks =  marks

#     def display_details(self):
#         print(f'Name : {self.name} Age : {self.age} Marks : {self.marks}')

# detils = Student("Sachin",25,90)
# detils.display_details()

# 26. Create a BankAccount class with deposit(), withdraw(), and check_balance() methods.

# class BankAccount:
#     def __init__(self,balance = 0):
#         self.balance = balance

#     def deposit(self,amount):
#         if amount <= 0:
#             print("Deposit amount must be positive")
#         else:
#             self.balance += amount
#             print(f'Deposited : {amount}')

#     def withdraw(self,amount):
#         if amount <= 0:
#             print("Withdrawl amount must be positve")
#         elif amount > self.balance:
#             print("insufficient Balance")
#         else:
#             self.balance -= amount
#             print("Withdrawl",amount)

#     def check_amount(self):
#         print(f"Current Balance : {self.balance}")

# account = BankAccount(10000)
# account.deposit(2000)
# account.withdraw(5000)
# account.check_amount()

# # 27. Demonstrate single inheritance using a Person class and an Employee class.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name",self.name)
#         print("Age",self.age)

# class Employee(Person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age)
#         self.salary = salary

#     def display_epm(self):
#         self.display()
#         print("Salary",self.salary)

# emp = Employee("Alice",25,89000)
# emp.display_epm()

# 28. Demonstrate method overriding and polymorphism with two different classes.

# class Dog:
#     def sound(self):
#         print("Dog barsk")

# class Cat:
#     def sound(self):
#         print("Cat Mew")

# # dog = Dog()
# # cat = Cat()

# # dog.sound()
# # cat.sound()

# animals = [Dog(),Cat()]
# for animal in animals:
#     animal.sound()

# 29. Create a class with a class variable, an instance variable, a class method, and a static method./

# class Student:
#     school = "Dauji Publicj school" # class Variable

#     def __init__(self,name,age):
#         #instance variable
#         self.name = name
#         self.age = age

#     # Instance Method
#     def display(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)

#     @classmethod
#     def change_school(self,new_school):
#         self.school = new_school

#     @staticmethod
#     def greet():
#         print("Welcome to the school!")

# s1 = Student("Alice",21)
# s1.display()

# print("School:", Student.school)

# Student.change_school("XYZ School")
# print("Updated School : ",Student.school)

# Student.greet()

# 30. Create an Employee class that uses @property to validate salary and raises a ValueError for negative values.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary can not be negative")
        self._salary = value

emp = Employee("Alice",55000)
print(emp.salary)

emp.salary = 60000
print(emp.salary)

# emp.salary = -1000