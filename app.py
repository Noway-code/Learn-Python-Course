# External Imports

# ====================
# Chapter 1: Getting Started
# ====================
# print("hello world")
#
# print("hello world")
#
# character_name = "John"
#
# character_age = 34
#
# print("Hello " + character_name + "!" + " How are you?" + " I hope you are doing well." + " I am doing well too." + " I am just learning Python."
# + "I am " + str(character_age) + " years old.")
#
# character_name = "Tom"
#
# print("Hello " + character_name + "!" + " How are you?" + " I hope you are doing well." + " I am doing well too." + " I am just learning Python."
# + "I am " + str(character_age) + " years old.")
#
# character_age = 50
#
# print("Hello " + character_name + "!" + " How are you?" + " I hope you are doing well." + " I am doing well too." + " I am just learning Python."
# + "I am " + str(character_age) + " years old.")
#
# character_male = True
#
# print("Hello " + character_name + "!" + " How are you?" + " I hope you are doing well." + " I am doing well too." + " I am just learning Python."
# + "I am " + str(character_age) + " years old." + " I hope you are doing well." + str(character_male))

# ====================
# Chapter 2: Working with Strings
# ====================
# print("Giraffe\nAcademy")  # This is how to print a new line
# print("Giraffe\"Academy")  # This is how to print a double quote
#
# phrase = "Giraffe Academy"
# print(phrase + " is cool")  # This is how to concatenate strings
# print(phrase.lower())  # This is how to convert a string to lower case
# print(phrase.upper())  # This is how to convert a string to upper case
# print(phrase.isupper())  # This is how to check if a string is upper case
# print(phrase.upper().isupper())  # This is how to check if a string is upper case
# print(len(phrase))  # This is how to get the length of a string
# print(phrase[0])  # This is how to get the first character of a string (0 based index)
# print(phrase.index("G"))  # This is how to get the index of first occurrence of a character
# print(phrase.index("Acad"))  # This is how to get the index of first occurrence of a sequence of characters
# print(phrase.replace("Giraffe", "Elephant"))  # This is how to replace a string with another string
# print(phrase.replace("Giraffe", "Elephant").replace("Academy", "School")
#       .replace("Elephant", "Something"))  # This is how to replace a string with another string multiple times
# ====================
# Chapter 3: Working with Numbers
# ====================
# print("Chapter 3: Working with Numbers")
# print(2)  # This is how to print a number
# print(2.0987)  # This is how to print a decimal number
# print(-2.0987)  # This is how to print a negative number
# print(3 + 4.5)  # This is how to add two numbers
# print(str(3 * 4 + 5) + " This is my favorite")  # This is how to convert a number to a string
# # print(3 * 4 + " This is my favorite")  # This does not work because you cannot concatenate a number with a string
#
# print(10 % 3)  # This is how to get the remainder of a division
# my_num = 5
#
# print(pow(3, 2))  # This is how to raise a number to a power
# print(max(4, 6))  # This is how to get the maximum of two numbers
# print(min(4, 6))  # This is how to get the minimum of two numbers
# print(round(3.50))  # Rounds up from 3.5 to 4
# print(round(3.49))  # Rounds down from 3.49 to 3
#
# # Using the math library
# print(floor(3.7))  # Always rounds down
# print(ceil(3.7))  # Always rounds up
# print(sqrt(36))  # This is how to get the square root of a number
# ====================
# Chapter 4: Getting Input from Users
# ====================
#
# print("Chapter 4: Getting Input from Users")
# stdin = input("Enter your name: ")
# print("Hello " + stdin + "!")
# print("You are " + stdin + " years old.")
# stdin = input("Enter your age: ")

# ====================
# Chapter 5: Building a Basic Calculator
# ====================

# print("Chapter 5: Building a Basic Calculator")
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
#
# print(result)

# ====================
# Chapter 7: Lists
# ====================
#
# print("Chapter 7: Lists")
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]  # This is how to create a list
# print(friends)  # This is how to print a list
# print(friends[1:3])  # This is how to print a range of elements in a list
# friends[1] = "Mike"  # This is how to modify an element in a list
# print(friends[:])  # This prints infinite range of elements in a list
# print(friends[2:])  # This prints everything from the 3rd element to the end of the list

# ====================
# Chapter 8: List Functions
# ====================

# print("Chapter 8: List Functions")
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers)  # This is how to add a list to another list (does not have to be the same type)
# friends.append("Creed")  # This is how to add an element to a list
# print(friends)
#
# friends.insert(1, "Kelly")  # This is how to insert an element at a specific index
#
# friends.remove("Jim")  # This is how to remove an element from a list
# print(friends)
#
# friends.clear()  # This is how to remove all elements from a list
# print(friends)
#
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#
# friends.pop()  # This is how to remove the last element from a list, stack ideology
# print(friends)
#
# # print(friends.index("d"))  # This is how to get the index of an element in a list
# print("Jim at: " + str(friends.index("Jim")))  # This is how to get the index of an element in a list
# friends.append("Jim")
# print(friends)  # This is how to get the index of an element in a list
# print(friends.count("Jim"))  # This is how to count the number of occurrences of an element in a list (non-existent element returns 0)
#
# friends.sort()  # This is how to sort a list
# print(friends)
#
# lucky_numbers.sort()  # This is how to sort a list
# print(lucky_numbers)
#
# lucky_numbers.reverse()  # This is how to reverse a list
# print(lucky_numbers)
#
# friends2 = friends.copy()  # This is how to copy a list
# print(friends2)
# ====================
# Chapter 9: Tuples
# ====================

# print("Chapter 9: Tuples")
#
# coordinates = (4, 5)  # This is how to create a tuple
# print(coordinates[0])  # This is how to access an element in a tuple.
# # A tuple is a data structure that is used to store an ordered collection of items.
# # Tuples are immutable, you cannot change the elements in a tuple.
# coordinates = [(4, 5), (6, 7), (80, 34)]  # This is how to create a list of tuples
# # tuple vs list: Tuples are immutable, lists are mutable. Tuples are used to store related pieces of information.
# # pretty niche use case, but it is useful in some cases.

# ====================
# Chapter 10: Functions
# ====================

# print("Chapter 10: Functions")
#
#
# def say_hi(name, age): # def is the keyword to define a function
#     print("Hello " + name + "!" + " You are " + str(age) + " years old.") # This is how to define a function
#
#
# return not necessary in python, but it is useful in some cases to return a value from a function
#
# print("Top")
# say_hi("Mike", 35)
#
# say_hi("Steve", 70)
# print("Bottom")
#

# ====================
# Chapter 11: Return Statement
# ====================
#
# print("Chapter 11: Return Statement")
#
#
# def cube(num):
#     return num * num * num  # This is how to return a value from a function
#
#
# result = cube(4)
# print(result)

# ====================
# Chapter 12: If Statements
# ====================

# print("Chapter 12: If Statements")
#
# boolTest = False
#
# if boolTest:
#     print("It is true")
# else:
#     print("It is false")
#
# boolTest = True
#
# if boolTest:
#     print("It is true")
# else:
#     print("It is false")
#
# is_male = True
# is_tall = True
#
# if is_male and not is_tall:  # and, or, not are the logical operators
#     print("You are a male or tall or both")
# else:
#     print("You are neither")

# ====================
# Chapter 13: If Statements & Comparisons
# ====================

# print("Chapter 13: If Statements & Comparisons")
#
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:  # This is how to compare numbers
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(3, 4, 5))
#
#
# def max_num2(num1, num2, num3):
#     if num1 == num2 and num1 == num3:  # This is how to compare numbers
#         return "All numbers are equal"
#     elif num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num2(4, 3, 3))


# ====================
# Chapter 14: Building a better Calculator
# ====================

# print("Chapter 14: Building a better Calculator")
#
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
# result = 0
#
# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "/":
#     result = num1 / num2
# elif op == "*":
#     result = num1 * num2
# else:
#     result = "Invalid operator"
#
# print(result)

# ====================
# Chapter 15: Dictionaries
# ====================

print("Chapter 15: Dictionaries")

monthConversions = {  # This is how to create a dictionary (like a map in Java)
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])  # This is how to get a value from a dictionary
print(monthConversions.get("Dec"))  # This is how to get a value from a dictionary
print(monthConversions.get("Luv", "Not a valid key"))  # This is how to get a default value for a non-existent key (Not a valid key)
print(monthConversions.get("Luv"))  # This is how to get a default value for a non-existent key (None)

# Dictionary keys are immutable, but the values can be anything.
# ====================
# Chapter 16: While Loop
# ====================

# print("Chapter 16: While Loop")


# ====================
# Chapter 17: Building a Guessing Game
# ====================

# print("Chapter 17: Building a Guessing Game")


# ====================
# Chapter 18: For Loop
# ====================

# print("Chapter 18: For Loop")


# ====================
# Chapter 19: Exponent Function
# ====================

# print("Chapter 19: Exponent Function")


# ====================
# Chapter 20: 2D Lists & Nested Loops
# ====================

# print("Chapter 20: 2D Lists & Nested Loops")


# ====================
# Chapter 21: Building a Translator
# ====================

# print("Chapter 21: Building a Translator")


# ====================
# Chapter 22: Comments
# ====================

# print("Chapter 22: Comments")


# ====================
# Chapter 23: Try/Except
# ====================

# print("Chapter 23: Try/Except")


# ====================
# Chapter 24: Reading Files
# ====================

# print("Chapter 24: Reading Files")


# ====================
# Chapter 25: Writing to Files
# ====================

# print("Chapter 25: Writing to Files")


# ====================
# Chapter 26: Modules & Pip
# ====================

# print("Chapter 26: Modules & Pip")


# ====================
# Chapter 27: Classes & Objects
# ====================

# print("Chapter 27: Classes & Objects")

# ====================
# Chapter 28: Building a Multiple Choice Quiz
# ====================

# print("Chapter 28: Building a Multiple Choice Quiz")


# ====================
# Chapter 29: Object Functions
# ====================

# print("Chapter 29: Object Functions")


# ====================
# Chapter 30: Inheritance
# ====================

# print("Chapter 30: Inheritance")


# ====================
# Chapter 31: Python Interpreter
# ====================

# print("Chapter 31: Python Interpreter")

# ====================
# The End of the Road
# ====================
