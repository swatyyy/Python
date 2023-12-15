answer = 5

print("Please guess number between 1 and 10:")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

# if guess< answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("you've guessed it right")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done,you've guessed it right")
#     else:
#         print("sorry, Try another time")
# else:
#     print("you got it correct")
