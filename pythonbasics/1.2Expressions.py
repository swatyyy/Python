# 🔹 What is an Expression?
#
# An expression in Python is any combination of values, variables, operators, and function calls that produces a result.
#
# 👉 Simply put: An expression is something Python can evaluate to a value.
#
# ✅ Examples:
# 5 + 3              # → 8 (arithmetic expression)
# x = 10
# x * 2              # → 20 (variable + operator)
# len("hello")       # → 5 (function call expression)
# x > 5 and x < 20   # → True (logical expression)
#
# 🔑 Don’t Forget Things about Expressions
#
# Expressions always return a value
#
# Even print(2 + 3) → evaluates 2 + 3 first (which is 5) then prints it.
#
# Expressions can be simple or complex
#
# Simple → 7
#
# Complex → (x + y) * (a / b) - len(name)
#
# Expressions are different from Statements
#
# Expression → produces a value (2 + 3)
#
# Statement → does something (like assignment x = 5, loop, if).
#
# Assignment (=) is not part of an expression in Python
#
# Unlike some languages (C, JavaScript), in Python:
#
# x = 5   # Statement (not an expression!)
#
#
# Operator precedence matters (PEMDAS rule: Parentheses, Exponent, Multiply/Divide, Add/Subtract).
#
# result = 2 + 3 * 4    # → 14, not 20
# result = (2 + 3) * 4  # → 20
#
#
# Expressions can include function calls, comprehensions, and even nested expressions.
#
# [x**2 for x in range(5)]   # expression that builds a list
#
# 🔹 Rules for Expressions
#
# ✔ Can include literals, variables, operators, functions
# ✔ Must follow syntax rules (no missing brackets, quotes, etc.)
# ✔ Respect operator precedence and associativity
# ✔ Use parentheses for clarity
# ✔ Expressions cannot directly assign values (assignment is a statement)
#
# 🔑 Super Quick Mnemonic
#
# 👉 “Expressions = Evaluate to a Value”