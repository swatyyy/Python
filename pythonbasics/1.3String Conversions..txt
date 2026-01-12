# 🔹 What is String Conversion?
#
# String conversion means changing other data types (like numbers, boolean) into strings so they can be used as text.
#
# This is often needed when printing messages, writing to files, or combining different types.
#
# 1️⃣ Converting Numbers to Strings
#
# Use the str() function.
#
# age = 25
# age_str = str(age)
# print(age_str)          # "25"
# print(type(age_str))    # <class 'str'>
#
#
# Don’t forget:
#
# str() works for int, float, complex, boolean.
#
# Useful in concatenation with other strings:
#
# name = "Alice"
# print("Age: " + str(age))  # Works
#
# 2️⃣ Converting Strings to Numbers
#
# String → int
#
# num_str = "100"
# num = int(num_str)
# print(num + 50)  # 150
#
#
# Don’t forget: The string must represent a valid integer, otherwise it will give ValueError.
#
# String → float
#
# num_str = "3.14"
# num = float(num_str)
# print(num + 2)  # 5.14
#
#
# Don’t forget: Works for decimal numbers too.
#
# String → complex
#
# c_str = "2+3j"
# c_num = complex(c_str)
# print(c_num)  # (2+3j)
#
# 3️⃣ Converting Boolean to String
# flag = True
# flag_str = str(flag)
# print(flag_str)  # "True"
#
# 4️⃣ Rules & Important Points
#
# Always valid formats → Conversion only works if the string represents a valid value of target type.
#
# int("25")   # ✅ works
# int("25.5") # ❌ ValueError
#
#
# Use str() for concatenation → You cannot combine string + number directly:
#
# print("Age: " + 25)   # ❌ Error
# print("Age: " + str(25))  # ✅ Works
#
#
# Python is strict about types → Explicit conversion is often needed.
#
# Use repr() when you want a string that shows the exact representation of an object.
#
# x = 10
# print(str(x))   # "10"
# print(repr(x))  # "10" (same for int, different for strings with quotes)
#
#
# Float → int conversion truncates → it does not round:
#
# x = int(3.99)
# print(x)  # 3
#
# 🔑 Mnemonic to Remember String Conversions
#
# “STRINGS Talk Numbers Clearly”
#
# STR → str()
#
# T → Type conversion
#
# Numbers → int, float, complex
#
# Clearly → Always valid format & explicit