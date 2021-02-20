ingredient1 = "chicken"
ingredient2 = "rice"

Michsays = input ("What is inside this hawker chicken rice?")

if (ingredient1 == Michsays or ingredient2 == Michsays):
    print("correct!")
else:
    print("look again!")

MichInput = input("How much is the hawker chicken rice?")
michAnswer = float(MichInput)
if michAnswer == 3.5:
    print("the price is right!")
if michAnswer > 3.5:
    print("hmm that may be too expensive! sad")
if michAnswer < 3.0:
    print("wow thats peanuts")


