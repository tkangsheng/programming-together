class Rectangle:
    width: float
    height: float
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    # ToString()
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        raise NotImplementedError

    def get_amount_inside(self):
        raise NotImplementedError

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_side(self):
        raise NotImplementedError

shapeA = Rectangle(3, 4)
shapeB = Rectangle(5, 6)
print(shapeA)
print(shapeB)
