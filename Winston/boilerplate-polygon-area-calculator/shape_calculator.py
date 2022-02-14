class Rectangle:
    width : float
    length : float

    def __init__(self, input_width: float, input_height: float) -> None:
        self.width = input_width
        self.height = input_height

    # ToString()
    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, input_width: float):
        self.width = input_width

    def set_height(self, input_height: float):
        self.height = input_height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.height*2) + (self.width*2)

    def get_diagonal(self):
        return (self.height**2 + self.width**2) ** 0.5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture_width = '*' * self.width
        for i in range(self.height):
            picture += picture_width
            picture += '\n'
        return picture

    def get_amount_inside(self, smaller_shape):
        return (self.width // smaller_shape.width) * (self.height // smaller_shape.height)

class Square(Rectangle):
    def __init__(self, input_side: float) -> None:
        super().__init__(input_side, input_side)

    def set_side(self, input_side: float):
        self.width = input_side
        self.height = input_side

    def __str__(self) -> str:
        return f'Square(side={self.width})'