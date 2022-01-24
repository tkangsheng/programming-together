class Rectangle:
    width : float
    height : float
    def __init__(self, width : float, height : float) -> None:
        self.width = width
        self.height = height

    # ToString()
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self):
        raise NotImplementedError

    def set_height(self):
        raise NotImplementedError

    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError

    def get_diagonal(self):
        raise NotImplementedError

    def get_picture(self):
        raise NotImplementedError

    def get_amount_inside(self):
        raise NotImplementedError

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_side(self):
        raise NotImplementedError

a = Rectangle(3, 4)
b = Rectangle(5, 6)
print(a)
print(b)