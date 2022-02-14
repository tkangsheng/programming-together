# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
    
#     # take note of "self.mileage:,"" for formatting of integers grouped by thousands
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage:,} miles."

# # Can use underscore to break up large numbers
# # Can put in specific parameter so that it's explicit
# blue_car = Car(color="blue", mileage=20_000)
# red_car = Car("red", 30000)

# print(blue_car)
# print(red_car)

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

test = GoldenRetriever("ab", 1)
print(test.dance())