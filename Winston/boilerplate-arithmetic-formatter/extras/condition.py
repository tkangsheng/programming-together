
a = 4
condition = a > 5

print(condition)
print(type(condition))


example_list = [1, 2]  # mutable
example_tuple = (1, 2)  # immutable

example_list.append(3)
print(example_list)

topic = "dataTypes"


class ComplexNumber:
    real: float = 0.0
    imaginary: float = 0.0

    def __init__(self, realValue: float, imaginaryValue: float) -> None:
        self.real = realValue
        self.imaginary = imaginaryValue

    def toString(self) -> str:
        return f"{self.real} + {self.imaginary}i"


examples_as_list = [
    ("bool", True),
    ("int", 1),
    ("float", 1.0),
    ("str", 'this is a string'),
    ("ComplexNumber", ComplexNumber(1, 3.5))
]

examples_as_dictionary = {
    "bool": True,
    "int": 1,
    "float": 1.0,
    "str": 'this is a string',
    "ComplexNumber": ComplexNumber(1, 3.5),
    "list": [1, 3, 4],
    "tuple": (1, 5, 6),
    "dict": {"key1": "value1"}
}

# "1 + 3.5i"
print(examples_as_dictionary["ComplexNumber"].toString())
print(1 == 1.0)