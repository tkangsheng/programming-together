# strings are immutable
name = "Winston"

try:
    name[0] = 'A' # will get exception
except:
    print("name[0] = 'A' will fail")

# lists are mutable
numbers = [ 2, 3, 5]
numbers[0] = 17
print(numbers) # [17, 3, 5]