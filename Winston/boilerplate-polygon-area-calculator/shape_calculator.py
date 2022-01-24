class Rectangle:
    width : float
    height : float
    def __init__(self, input_width : float, input_height : float) -> None:
        self.width = input_width
        self.height = input_height

    # ToString()
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

a = Rectangle(3, 4)
b = Rectangle(5, 6)
print(a)
print(b)