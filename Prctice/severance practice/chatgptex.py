#Odd Or Even

x= int(input ("Enter the number"))

if x % 2== 0:
    print("Its Even number daw")
else:
    print("Its odd daw")

print("Done")

#Largest of Three
#Ask the user for 3 numbers and print the largest one.

q= int(input ("Enter the first number"))
w= int(input ("Enter the Second number"))
o= int(input ("Enter the Third number"))

if q>w>o: # this is wrong -The condition q > w > o means q > w AND w > o.
#This only works if numbers are in strict descending order. Example: q=9, w=5, o=1.

#But if you have numbers like q=9, w=1, o=5, your code won’t correctly say q is the largest.
#Same issue with w>o>q.
    print(f"{q} is the largest number")
elif w>o>q:
    print(f"{w} is the largest number")
else:
    print(f"{o} is the largest number")

print ("Done")

✅ Correct Way:

Check each number individually:

#q = int(input("Enter the first number: "))
#w = int(input("Enter the second number: "))
#o = int(input("Enter the third number: "))

#if q >= w and q >= o:
#   print(f"{q} is the largest number")
#elif w >= q and w >= o:
#    print(f"{w} is the largest number")
#else:
# print(f"{o} is the largest number")

#print("Done ✅")

#🔎 Even Shorter Pythonic Version:

#You can use the built-in max() function:

q = int(input("Enter the first number: "))
w = int(input("Enter the second number: "))
o = int(input("Enter the third number: "))

largest = max(q, w, o)
print(f"{largest} is the largest number")
print("Done ✅")


#Pallindrome checker
q = input ("Enter a word/number")
i = len(q)

for x in range(i):
    w = q[x]
    print(w)

