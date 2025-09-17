# User input is a way to let your Python program get data from the person running the program.
#
# In Python, the built-in function input() is used to take input from the user.
#
# Always returns a string, even if the user types a number.
#
# 1️⃣ Basic Usage
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
#
#
# Output Example:
#
# Enter your name: Alice
# Hello, Alice!
#
#
# Don’t forget:
#
# The text inside input("...") is called the prompt.
#
# Whatever the user types is stored as a string.
#
# 2️⃣ Taking Number Input
#
# Since input() always returns a string, you must convert it to the correct type if you want numbers:
#
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
#
# print("Your age:", age)
# print("Your height:", height)
#
#
# Don’t forget:
#
# Use int() for integers, float() for decimal numbers.
#
# If user enters invalid input (like letters instead of numbers), Python will give ValueError.
#
# 3️⃣ Rules & Important Points
#
# Always store input in a variable
#
# user_name = input("Enter your name: ")  # ✅ correct
#
#
# Input is always a string by default
#
# Convert to appropriate type if needed (int(), float(), bool())
#
# Prompt message is optional but helps the user understand what to type
#
# name = input()  # works, but no prompt
#
#
# Avoid assuming the user enters valid data → can use try-except for safety.
#
# 4️⃣ Example with Validation
# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)
# except ValueError:
#     print("Please enter a valid number!")
#
#
# Don’t forget: Always handle invalid input if your program is user-facing.
#
# 🔑 Mnemonic to Remember User Input
#
# “INPUT = I Need Prompt To Understand Text”
#
# I → Input
#
# N → Needs prompt
#
# P → Prompt displayed to user
#
# T → Text returned (always a string)