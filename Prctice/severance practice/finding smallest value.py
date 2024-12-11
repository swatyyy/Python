smallest = None
print('Before')
for n in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
    print(smallest,n)
print('After',smallest)

#quest
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)