# What are the main features of Python?
# Answer:  Python is a high-level, interpreted, general-purpose programming language. It is popular because of its simple syntax and readability.

# Main features of Python:
# 1. Easy to learn: Simple and readable syntax.
# 2. Interpreted: Python code is executed by the Python runtime.
# 3. Dynamically typed: We don't need to declare variable types explicitly.
# 4. Object-oriented: Supports classes, objects, inheritance, and polymorphism.
# 5. Cross-platform: Runs on Windows, Linux, and macOS.
# 6. Large standard library: Provides built-in modules for many tasks.
# 7. Automatic memory management: Python manages memory automatically.

# What are the differences between a list, tuple, set, and dictionary?

# Feature      	List	      Tuple	     Set	               Dictionary
# Syntax	     []	           ()	     {}	                   {key: value}
# Ordered     	Yes	           Yes	     No guaranteed order	Yes
# Mutable     	Yes	           No	    Yes	                    Yes
# Duplicates  	Allowed	     Allowed	Not allowed	          Keys must be unique
# Access	        Index	      Index	    No indexing            	Key

# #List 
# fruits = ["apple","banana","papaya"]
# fruits.append("mango")
# print(fruits)

# # Tuple
# cordiantes = (10,20)
# print(cordiantes[0])

# # Set

# numbers = {1,2,3,4,5}
# print(numbers)

# # Dictionary
# stduent = {"name":"Sachin","age":24}
# print(stduent)

# What is the difference between mutable and immutable objects?

# Mutable: An object whose contents can be changed after creation.
# Immutable: An object whose contents cannot be changed after creation.

#mutable
# numbers = [10,20,30,40]
# numbers.append(50)
# print(numbers)

# # immutable

# name = "Python"
# name = name + " Programming"
# print(name)

# What is the difference between == and is?

# == checks whether two objects have equal values.
# is checks whether two references point to the same object.

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# print(a == b)

# 4. Explain shallow copy and deep copy with examples.
# Shallow copy: Creates a new outer object, but nested objects are shared.
# Deep copy: Creates a new outer object and recursively copies nested objects.

# import copy

# original = [[1,2],[3,4]]

# shallpw = copy.copy(original)
# deep = copy.deepcopy(original)

# shallpw[0][0] = 99
# print(shallpw)
# print(deep)

# What is the difference between append(), extend(), and insert()?
# All three methods modify a list, but they work differently.

# example
#append() - Adds one item at the end
# a = [1,2]
# a.append(3)
# print(a)

# #extend() - Adds each element of an iterable
# b = [1,2]
# b.extend([3,4])
# print(b)

# #insert() - Adds an item at a specified index
# c = [1,2]
# c.insert(1,100)
# print(c)

# Q7. What is the difference between remove(), pop(), and del?
# These are used to remove elements from a list.

# #remove - removes the first matching value
# a = [10,20,30,40]
# a.remove(20)
# print(a)

# ## pop(): removes and returns an element
# b = [10,20,30,40]
# b.pop()
# print(b)

# # del: deletes an item or a slice
# c = [10,20,30]
# del c[0]
# print(c)


# 5. What are *args and **kwargs?
# *args =  allows a function to accept a variable number of positional arguments. These arguments are collected into a tuple.
# **kwargs = allows a function to accept a variable number of keyword arguments. These arguments are collected into a dictionary.

# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(10,20,30))

# def display_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} : {value}')

# display_details(name = "Sachin", age = 25)

# Explain list comprehension and dictionary comprehension.

# 7. Explain list comprehension and dictionary comprehension.
# Definition: Comprehensions provide a concise way to create lists or dictionaries from iterables, optionally applying transformations and filtering conditions.

# List comprehension example:

# sqaures = [x**2 for x in range(1,6)]
# print(sqaures)

# even_numbers = [x for x in range(1,10) if x % 2 == 0]
# print(even_numbers)

# Dictionary comprehension example

# sqaures = {x: x**2 for x in range(1,11)}
# print(sqaures)

# Q9. What is the difference between local, global, and nonlocal variables?
# Answer:
# - Local variable: Defined inside a function and normally accessible within that function.
# - Global variable: Defined at module level and accessible throughout the module.
# - Nonlocal variable: Refers to a variable in an enclosing function scope, excluding the global scope.

# example
# x = 100 # global

# def outer():
#     y = 200 # local

#     def inner():
#         nonlocal y # nonlocal
#         y = 300
#         print(y)

#     inner()
#     print(y)

# outer()
# print(x)

# Q10. What is the difference between break, continue, and pass?
# Keyword	       Meaning
# break	        Terminates the nearest loop
# continue   	Skips the current iteration
# pass	        Does nothing; acts as a placeholder

# for i in range(1,6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)

# Q12. What is the difference between range() and xrange()?
# range() is used to generate a sequence of numbers.
# In Python 3, xrange() does not exist. In Python 2, range() returned a list, 
# while xrange() produced numbers lazily without creating the complete list in advance.

# for i in range(1,5):
#     print(i)

# Q13. What is the difference between a module and a package?
# - Module: A single Python file containing code such as functions, classes, or variables.
# - Package: A directory used to organize related Python modules and subpackages.

# Q14. What is exception handling? Explain try, except, else, and finally.

# Exception handling allows us to handle runtime errors so the program can respond appropriately instead of terminating unexpectedly.
# - try: Contains code that might raise an exception.
# - except: Handles a matching exception.
# - else: Runs if no exception occurs in the try block.
# - finally: Runs whether an exception occurs or not, including when an exception is handled.

# try:
#     a = 10
#     b = 2
#     result = a / b
# except ZeroDivisionError:
#     print("Can divided by zero")
# else:
#     print("Result : ",result)
# finally:
#     print("Excuation Completed")

# Q15. What is the difference between syntax errors and exceptions?

# - Syntax error: Occurs when code violates Python's grammar rules.
# - Exception: An error raised during program execution, even though the code is syntactically valid.

# if 20 > 10
#    print("Hello") # Syntax error

# a = 10
# b = 0
# print(a / b)  # exception

# Q16. What are lambda functions? When would you use them?

# A lambda function is a small anonymous function defined using the lambda keyword.
#  It can contain a single expression.

# squares = lambda x:x**2
# print(squares(6))
# students = [
#     {"name": "Amit", "marks": 80},
#     {"name": "Ravi", "marks": 95},
#     {"name": "Neha", "marks": 70}
# ]

# students.sort(key = lambda student:student["marks"])
# print(students)

# Q17. What is the difference between sort() and sorted()?

# - sort() sorts a list in place and returns None.
# - sorted() returns a new sorted list and works with any iterable.

#sort()
# numbers = [10,30,20]
# result = numbers.sort()
# print(numbers)
# print(result)

#sorted()

# numbers = [30,20,40,10]
# result = sorted(numbers)
# print(numbers)
# print(result)

# Q18. What is the difference between None, False, and 0?

# - None represents the absence of a value.
# - False is a Boolean value representing false.
# - 0 is the integer zero.

# a = None
# b = False
# c = 0
# print(a is None)
# print (b == False)
# print (c == 0)

# Q19. What are Python's identity, membership, and comparison operators?

# Python has several operator categories.
# Category	    Operators	            Purpose
# Comparison	==, !=, >, <, >=, <=	Compare values
# Identity	    is, is not	            Check object identity
# Membership	in, not in	            Check whether an item belongs to a collection

# a = 10
# b = 20

# print(a < b)
# print( a == b)

# #identity

# x = None
# print(x is None)

# # Memebrship
# numbers = [10,20,30]
# print(20 in numbers)
# print(40 not in numbers)

# student = {"name": "Sachin", "age": 25}
# print("name" in student)
# print("Sachin" in student)

# Q20. How does Python manage memory? What is garbage collection?

# Python manages memory automatically. It allocates memory for objects and reclaims memory when objects are no longer needed.

# The main mechanisms include:
# 1. Reference counting: Tracks references to objects. When an object's reference count reaches zero, it can generally be reclaimed.
# 2. Garbage collection: The cyclic garbage collector can detect and collect unreachable objects that reference each other in cycles.
# 3. Memory allocation: Python uses its memory-management system to allocate memory for objects.

# import gc

# class Studenet:
#     pass

# student = Studenet()
# student = None