# 🔹 Numbers in Python
#
# Python supports different types of numbers to store numeric data.
#
# 1️⃣ Types of Numbers
#
# int (Integer)
#
# Whole numbers (no decimal point)
#
# Example:
#
# age = 25
# year = 2025
#
#
# Don’t forget: Integers can be positive, negative, or zero.
#
# float (Floating point)
#
# Numbers with decimal points
#
# Example:
#
# price = 99.99
# pi = 3.14159
#
#
# Don’t forget: Float division always produces a float.
#
# complex
#
# Numbers with real and imaginary parts
#
# Format: a + bj
#
# Example:
#
# z = 2 + 3j
# print(z.real)  # 2.0
# print(z.imag)  # 3.0
#
#
# Don’t forget: Use j for imaginary part, not i.
#
# 2️⃣ Numeric Operations (Arithmetic)
# Operator	Meaning	Example	Output
# +	Addition	5 + 3	8
# -	Subtraction	10 - 4	6
# *	Multiplication	2 * 3	6
# /	Division	10 / 2	5.0
# //	Floor Division	10 // 3	3
# %	Modulus (remainder)	10 % 3	1
# **	Exponentiation	2 ** 3	8
#
# Don’t forget:
#
# / always returns a float
#
# // returns integer part only
#
# % gives the remainder
#
# 3️⃣ Rules & Important Points
#
# Numbers are immutable → Once a number is created, its value cannot be changed.
#
# x = 5
# x = x + 1   # creates a new object 6, doesn’t change 5
#
#
# Python automatically selects the type based on the number you use.
#
# a = 10    # int
# b = 10.5  # float
#
#
# No size limit for integers → Python integers can grow as big as memory allows.
#
# Type conversion is possible → int ↔ float
#
# x = 5     # int
# y = float(x)  # convert to 5.0
# z = int(3.99) # convert to 3
#
#
# Complex numbers cannot be directly converted to int/float
#
# 🔑 Mnemonic to Remember Numbers
#
# “I Fought Complex Battles”
#
# I → Int
#
# Fought → Float
#
# Complex → Complex