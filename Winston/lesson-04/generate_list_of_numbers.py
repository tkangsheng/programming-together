import random

random_numbers = []
for i in range(0,10):
    generated_random_number = random.randint(0, 100)
    random_numbers.append(generated_random_number)

print(random_numbers)
