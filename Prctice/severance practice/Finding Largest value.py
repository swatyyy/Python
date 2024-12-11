#printing in a loop
zork = 0
print('Before', zork)
for n in [9,41,12,3,74,15]:
    zork= zork + 1
    print(zork, n)
print('After', zork)

#summing in a loop
zork = 0
print('Before', zork)
for n in [9,41,12,3,74,15]:
    zork= zork + n
    print(zork, n)
print('After', zork)

#finding average in a loop

sum = 0
count = 0
print('Before', sum, count)
for n in [9, 41, 12, 3, 74, 15]:
    sum = sum + n
    count = count + 1
    Avg = sum/count
    print(count,n,sum,int(sum/count))
print('After', int(Avg))

#finding the largest number  in a loop
num = 0
print('Before', num)
for n in [9, 41, 12, 3, 74, 15]:
    if n>num:
        num = n
        print(num)
print('After', num)