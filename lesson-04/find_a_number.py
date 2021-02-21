foundAThree = False
print('Before', foundAThree)
for number in [9, 41, 12, 3, 74, 15, 100, 1000, 123, 21]:
    if (number == 3):
        foundAThree = True
        print(foundAThree, number)
        break
    #insert 'break' to go out of the loop and move out of the loop (i.e. jump to line 11)
    #insert 'continue' to skip the rest of the iteration and go back to the first line of the loop (i.e. skip line 10 and jump to line 3)
    print(foundAThree, number)
print('After', foundAThree)

smallest_number_so_far = None
for number in [45, 60, 10, 7, 84, 0, 87, 56, 15, 3]:
    if smallest_number_so_far is None:
        smallest_number_so_far=number
    elif number<smallest_number_so_far:
        smallest_number_so_far=number
    print(smallest_number_so_far,number)
