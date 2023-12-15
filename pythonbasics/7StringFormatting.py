for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
"""Format Specifiers:

{0:2}, {1:3}, and {2:4} are format specifiers inside the string.
{0:2}: The first placeholder (index 0) is reserved for the value of i. The :2 indicates that it should be right-aligned with a width of 2 characters.
{1:3}: The second placeholder (index 1) is for the square of i, right-aligned with a width(space) of 3 characters.
{2:4}: The third placeholder (index 2) is for the cube of i, right-aligned with a width of 4 characters."""
print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7)) #12 means 15 digits after decimal point
print("Pi is approximately {0:12f}".format(22 / 7))#f means 6 digits after decimal point
print("Pi is approximately {0:12.50f}".format(22 / 7))#50f means 50 digits after decimal point. python compares whats important
#width or precision. So acc to Python, Precision is important so it ignores width-12 and adds 50 points after decimal - precision
print("Pi is approximately {0:52.50f}".format(22 / 7)) #When the precision (number of digits after the decimal point) is less than the specified width in formatting,
# #the output will still respect the width, but the extra space may be filled with leading zeros or whitespace.
#there's no difference in Output because - 50 decimals, plus the 3 and the dot make 52 characters.
#That's from memory; if it doesn't make sense, please paste in your code.
print("Pi is approximately {0:62.50f}".format(22 / 7)) #the right spaces after string approximaely is 12 ->62-50

print("Pi is approximately {0:<72.50f}".format(22 / 7)) #left alligned by 22 spaces
print("Pi is approximately {0:<72.54f}".format(22 / 7)) #the maximum precision is 51 to 53 so for the extra 3 digits we get 0's in last 3 digts after decimal point

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
