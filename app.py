# External Imports
import math
from Question import Question
from ChineseChef import ChineseChef

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

# print("Chapter 15: Dictionaries")
#
# monthConversions = {  # This is how to create a dictionary (like a map in Java)
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
#
# print(monthConversions["Nov"])  # This is how to get a value from a dictionary
# print(monthConversions.get("Dec"))  # This is how to get a value from a dictionary
# print(monthConversions.get("Love", "Not a valid key"))  # This is how to get a default value for a non-existent key (Not a valid key)
# print(monthConversions.get("Luv"))  # This is how to get a default value for a non-existent key (None)

# Dictionary keys are immutable, but the values can be anything.
# ====================
# Chapter 16: While Loop
# ====================

# print("Chapter 16: While Loop")
#
# i = 1
# while i <= 100:  # This is how to create a while loop
#     print(i)
#     i += 1  # This is how to increment a variable
#
# print("Done with loop")
# ====================
# Chapter 17: Building a Guessing Game
# ====================

# print("Chapter 17: Building a Guessing Game")
#
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not out_of_guesses:  # This is how to create a while loop
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses, you lose!")
# else:
#     print("You win!")
#
# ====================
# Chapter 18: For Loop
# ====================

# print("Chapter 18: For Loop")
#
# for e in "Giraffe Academy":  # Like a for each loop in Java. python assumes you want to iterate over the string and stores that value in e
#     print(e)
# # python is smart enough to know how you want to over the object passed.
# friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print(friend)
#
# # Wow, this is weird.
# for index in range(3, 10):
#     print(index)
#
# for index in range(len(friends)):
#     print(friends[index])  # printing ints always adds a new line
#     print(index, end='\n\n')  # These are weird ways to print an extra new line
#     print(str(index) + "\n")
#
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Not first")
#

# ====================
# Chapter 19: Exponent Function
# ====================

# print("Chapter 19: Exponent Function")
#
#
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result *= base_num
#     return result
#
#
# for i in range(1, 64):
#     print(raise_to_power(2, i))
#
#

# ====================
# Chapter 20: 2D Lists & Nested Loops
# ====================

# print("Chapter 20: 2D Lists & Nested Loops")
#
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# # number_grid = [
# #     [1, 2, 3], [4, 5, 6], [7, 8, 9],[0]
# # ]
#
# print(number_grid[0][0])  # This is how to access an element in a 2D list
# print(number_grid[2][1])  # This is how to access an element in a 2D list
# # basically, the first index is the row, the second index is the column
#
# for row in number_grid:
#     for col in row:
#         print(col)
#
# print(number_grid[3])

# ====================
# Chapter 21: Building a Translator
# ====================

# print("Chapter 21: Building a Translator")
#
#
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation += "G"
#             else:
#                 translation += "g"
#         else:
#             translation += letter
#     return translation
#
#
# print(translate(input("Enter a phrase: ")))
#
#
# ====================
# Chapter 23: Try/Except
# ====================

# print("Chapter 23: Try/Except")
#
# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

# ====================
# Chapter 24: Reading Files
# ====================

# print("Chapter 24: Reading Files")
#
# employeeFile = open("employees.txt", "r")  # Accepts two arguments, the file name and the mode (r, w, a, r+)
# # r = read, w = write, a = append, r+ = read and write
#
# print(employeeFile.readable())  # This is how to check if a file is readable
# # print(employeeFile.read())  # This is how to read a file, all subsequent reads will return an empty string
# # print(employeeFile.readline())  # This is how to read a line from a file, if you call it again, it will read the next line
# print(employeeFile.readlines())  # This is how to read all lines from a file

# ====================
# Chapter 25: Writing to Files
# ====================

# print("Chapter 25: Writing to Files")
#
# # employeeFile = open("employees.txt", "a")  # Accepts two arguments, the file name and the mode (r, w, a, r+). a = append
# employeeFile = open("index.html", "w")  # overwrites the file if it exists, creates a new file if it does not exist
#
# employeeFile.write("<p> Hello world </p>")  # This is how to write to a file
#
# employeeFile.close()  # This is how to close a file

# ====================
# Chapter 26: Modules & Pip
# ====================

# print("Chapter 26: Modules & Pip")
#
# # import useful_tools  # This is how to import a module
#
# # print(useful_tools.roll_dice(10))  # This is how to use a function from a module
# print(math.log(10))
# # you can find a list of python modules at https://docs.python.org/3/py-modindex.html
# # you can also install third party modules using pip (python package manager)
# # there are built-in modules, and third party modules that you can install using pip


# ====================
# Chapter 27: Classes & Objects
# ====================

# print("Chapter 27: Classes & Objects")
#
#
# class Student:  # This is how to create a class
#     def __init__(self, name, major, gpa, is_on_probation):  # This is how to create a constructor
#         self.name = name  # This is how to create an instance variable
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation
#
#     # self is a reference to the current instance of the class (like this in Java) and is used to access variables that belong to the class
#     # __init__ is a special function that is called when you create an object of a class (like a constructor in Java)
#     # You can also create functions in a class (like methods in Java) that can be called from an object of the class
#     # You can also create a function that returns a value (like a getter in Java) that can be called from an object of the class
#     # python does not have private variables, but you can use a single underscore to indicate that a variable is private\
#     # python is an object-oriented language, and everything in python is an object (like Java)
#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return "Name: " + self.name + ", Major: " + self.major + ", GPA: " + str(self.gpa) + ", On Probation: " + str(
#             self.is_on_probation)
#
#
# student1 = Student("Jim", "Business", 3.1, False)  # This is how to create an object
# student2 = Student("Pam", "Art", 2.5, True)  # This is how to create an object
#
# print(student1.name)  # This is how to access an instance variable
# print(student2.name)  # This is how to access an instance variable
# print(student1.on_honor_roll())  # This is how to call a function from an object
# print(student2.on_honor_roll())  # This is how to call a function from an object
# print(student1)  # This is how to print an object
# print(student2)  # This is how to print an object

# ====================
# Chapter 28: Building a Multiple Choice Quiz
# ====================
#
# print("Chapter 28: Building a Multiple Choice Quiz")
#
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
# ]
#
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]
#
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct")
#
#
# run_test(questions)

# ====================
# Chapter 29: Object Functions
# ====================

# print("Chapter 29: Object Functions")
#
#
# class Student:  # This is how to create a class
#     def __init__(self, name, major, gpa, is_on_probation):  # This is how to create a constructor
#         self.name = name  # This is how to create an instance variable
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation
#
#     # self is a reference to the current instance of the class (like this in Java) and is used to access variables that belong to the class
#     # __init__ is a special function that is called when you create an object of a class (like a constructor in Java)
#     # You can also create functions in a class (like methods in Java) that can be called from an object of the class
#     # You can also create a function that returns a value (like a getter in Java) that can be called from an object of the class
#     # python does not have private variables, but you can use a single underscore to indicate that a variable is private\
#     # python is an object-oriented language, and everything in python is an object (like Java)
#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False
#
#
# student1 = Student("Jim", "Business", 3.1, False)  # This is how to create an object
# student2 = Student("Pam", "Art", 2.5, True)  # This is how to create an object
#
# print(student1.name)  # This is how to access an instance variable
# print(student2.name)  # This is how to access an instance variable
# print(student1.on_honor_roll())  # This is how to call a function from an object
# print(student2.on_honor_roll())  # This is how to call a function from an object

# ====================
# Chapter 30: Inheritance
# ====================
#
# print("Chapter 30: Inheritance")
#
# myChef = ChineseChef()
# myChef.make_special_dish()
# myChef.make_fried_rice()
# myChef.make_chicken()
# myChef.make_salad()

# ====================
# The End of the Road
# ====================
