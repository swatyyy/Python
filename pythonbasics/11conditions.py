age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

"""
when comparing conditions using AND, Python will stop checking as soon as it finds a condition that is False

When comparing conditions using OR, Python will stop checking as soon sa it finds a condition that is True

"""
