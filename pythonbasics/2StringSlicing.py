# Slice-back or reverse string
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1] #python idioms
print(backwards)  #zyxwvutsrqponmlkjihgfedcba

backwards1 = letters[25:0:-1] #"""Slicing - Main rule of Slicing - Upto but not including the last index, 2. U should always use : for slicing"""
print(backwards1)  #zyxwvutsrqponmlkjihgfedcb - a is not included


#Negative Indexing in Strings - important topic
parrot = "Norwegian Blue"
#        -43210987654321
#        1
print(parrot[-14])

#slicing with Negative Numbers
#                   1
#         012345678901234
parrot = "Norwegian Blue"
#        -43210987654321
#        1

print(parrot[0:6])  # Norweg
print(parrot[-14:-8])  #note to yourself - we cannot go from -8:-14 - this is reverse order ..
# we can always do left from right and not right from left in negative selection

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl



#Using a step in SLICING
print(parrot[0:6:2])
# it will count from 0 to 5 in parrot and picks only words in 2's INTERVAL.. starts from 0.. so 0,2,4  index
#output - NRE

print(parrot[0:6:3])
# it will count from 0 to 5 in parrot and picks only words in 3's INTERVAL.. starts from 0.. so 0,3 index
#output - NW
#                    1         2
         #01234567890123456789012345
number = "9,223;372:036 854,775;807"
seperators = number[1::4] #Includes double colon - starts from 1 and picks every 4th character - dpnt countinue as 2 after forst slice and dont start with 0 again after the first slice
#means count it as 01123412341234
#no stop value here so slicing will continue till the end
print(seperators)  #output - ,;: ,;

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values]) #o/p -[9, 223, 372, 36, 854, 775, 807]
