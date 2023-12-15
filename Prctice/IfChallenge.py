name = input("Hi there,What's your Name?: ")
age = int(input("Hi {}, what is your age?: ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the holiday {}".format(name))
else:
    print("sorry you are not eligible for this holiday")
