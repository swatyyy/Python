
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
#         -65432109876543210987654321
#                2         1
backwards = letters[::-1]
print(backwards)

#create a sice which produces 'qpo'
back = letters[16:13:-1]
print(back)


#create a slice which produces 'edcba'
print(letters[4::-1])

#slice the string to produce the last 8 characters, in reverse order
print(letters[-8:26]) #stuvwxyz
#but to reverse
print(letters[:-9:-1])
