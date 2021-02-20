x = 0
while (x < 10):
    x += 1
    print(x)
    if ( x == 7 ):
        break
    elif (x == 4):
        print("x is 4")
        continue
    print('not 4 or 7')
print('loop done')