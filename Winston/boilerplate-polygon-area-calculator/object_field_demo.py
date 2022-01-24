class SpecialNumber:
    number = 1 # field or attribute

    def myMethod1(self, number: float):
        return number

    def myMethod2(self, number: float):
        return self.number

numberA = SpecialNumber()
result = numberA.myMethod2(3)
print(f'specialNumber returned {result}')