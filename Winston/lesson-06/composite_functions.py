def indexesOf(list):
    return range(len(list))

friends = ['joseph', 'glenn', 'sally']
print(indexesOf(friends))
print(range(3)) # [ 0, 1, 2 ]

# for number in range(1, 101):
#     print(number)

for n in indexesOf(friends):
    print(n)