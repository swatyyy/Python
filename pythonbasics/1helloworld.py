print('Hello, World!')

#Constants, Keywords,Reserved Words,variables

# 1. Constants
#
# Python does not have true constants (unlike Java or C++).
#
# By convention, variables written in ALL_CAPS are treated as constants.
#
# PI = 3.14159
# GRAVITY = 9.8
#
#
# Don’t Forget:
#
# Constants are just variables (you can reassign them, but you shouldn’t).
#
# Used for values that should not change in your program.
#
# 🔹 2. Keywords
#
# Keywords are special reserved words in Python that have predefined meaning.
#
# Example: if, else, for, while, True, False, None, class, def.
#
# if True:
#     print("This is a keyword example")
#
#
# Don’t Forget:
#
# You cannot use keywords as variable names.
#
# Keywords define the structure and flow of your program.
#
# Check all keywords in Python with:
#
# import keyword
# print(keyword.kwlist)
#
# 🔹 3. Reserved Words
#
# Reserved words = keywords + some words reserved for future use.
#
# Example: async, await (in older versions they were reserved, later became keywords).
#
# Don’t Forget:
#
# Don’t use reserved words as identifiers (variable/function names).
#
# They are part of the Python grammar.
#
# 🔹 4. Variables
#
# Variables are containers for data.
#
# name = "Alice"
# age = 25
# height = 5.6
#
#
# Python is dynamically typed → you don’t declare type explicitly.
#
# Don’t Forget Rules for Naming Variables:
#
# Must start with a letter or _ (underscore).
#
# Cannot start with a number (2age = 25 ❌).
#
# Can contain letters, digits, underscore → student_name1 ✅.
#
# Case-sensitive → Name and name are different.
#
# Should not be a keyword or reserved word.
#
# 🔹 Important Points to Remember
#
# ✅ Constants → Convention only (ALL_CAPS).
# ✅ Keywords → Predefined, can’t be reused.
# ✅ Reserved words → Future-safe words, don’t use them.
# ✅ Variables → Dynamically typed, follow naming rules.
# ✅ Use meaningful variable names (good practice).