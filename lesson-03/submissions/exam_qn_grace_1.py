studentInput=input("2+2=")

x=0
try:
    x=float(studentInput)
except:
    print("That's not a number, try again!")
    #remember to assign back the same variable
    x=input("2+2=")
if x==2+2:
    print("Genius")
else:
    while x!=2+2: #'4' != 4
        print("Try again!")
        x=input("2+2=")
print("End")