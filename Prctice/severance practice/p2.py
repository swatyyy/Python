def fizzBuzz(n):
    while n>0:
        if n%3==0 and n%5==0:
            print('FizzBuzz')
        elif n%3==0:
            print('Fizz')
        elif n%5==0:
            print('Buzz')
        else:
            print(n)
        n-=1

X= input("Enter your number")
n = int(X)
fizzBuzz(n)