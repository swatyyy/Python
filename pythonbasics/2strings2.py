#                   1
#         012345678901234
parrot = "Norwegian Blue"
#        -43210987654321
#        1
"""Slicing - Main rule of Slicing - Upto but not including the last index, 2. U should always use : for slicing"""
# print(parrot[0:6])  # Norweg
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9]) #other way of doing the previous step
#
# print(parrot[10:14]) #Blue
# print(parrot[10:]) #Blue
#
# print(parrot[:6]) #Norweg
# print(parrot[6:]) #ian Blue
#
# print(parrot[:6] + parrot[6:]) Norwegian Blue
#
# print(parrot[:]) Norwegian Blue

# Slice-back
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]
print(backwards)


#Negative Indexing in Strings - important topic
parrot = "Norwegian Blue"
#        -43210987654321
#        1
print(parrot[-14])


print(parrot[10:13])
print(parrot[:6] + parrot[6:])
print(parrot[10:])
