

typeofInteger = type(4)
typeofFloat = type(4.1)
typeofString = type("four")
typeofString2 = type('four')
typeofType = type(typeofInteger)


print(typeofInteger)
print(typeofFloat)
print(typeofString)
print(typeofString2)
print(typeofType)

myInteger = 4
myFloat = 4.1
myString = 'four'

floatConvertedInteger = float(myInteger)
stringConvertedInteger = str(myInteger)
stringConvertedFloat = str(myFloat)

try:
    floatConvertedString = float(myString)
    print(f"floatConvertedString = float('{myString}') will NOT blow up")
except:
    print(f"floatConvertedString = float('{myString}') will blow up")

try:
    intConvertedString = int(myString)
    print(f"intConvertedString = int('{myString}') will NOT blow up")
except:
    print(f"intConvertedString = int('{myString}') will blow up")

try:
    intConvertedFloat = int(myFloat)
    print(f"intConvertedFloat = int({myFloat}) will NOT blow up")
except:
    print(f"intConvertedFloat = int({myFloat}) will blow up")

