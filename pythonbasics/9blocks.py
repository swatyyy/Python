for i in range(1, 13):
    print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*"*80)

""" This piece of code explains about how indentation works in Block of code.. Try to remove the space before print("*"*80)
 and check the result. if space is removed its outside for loop and prints * only in last line after the condition is executed"""

name = input("Please enter your name: ")
age = int(input("what is your age, {0} ".format(name))) #if the input is given as string as in twenty instead of 20 then this code wil throw error
print(age)

# if age >= 18:
#     print("you are old enough to vote")
# else:
#     print("please come back in {0} years".format(18-age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
