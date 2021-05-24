studentInput=input("2+2=")
x=studentInput
try:
    x=float(studentInput)
except:
    print("That's not a number, try again!")
if x==4:
    studentInput2=input("Correct! What is 4+5=")
    y=studentInput2
else: studentInput=input("2+2=")
while x!=4: studentInput=input("2+2=")
try:
    y=float(studentInput2)
except:
    print("That's not a number, try again!")
    studentInput=input("2+2=")
if y==9:
    print("Correct!")
else: studentInput2=input("4+5=")
print("End")

