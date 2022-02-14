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
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        picture_width = '*' * self.width
        picture = picture_width
        for i in range(self.height):
            picture += '\n'
            picture += picture_width
        return picture

    def get_amount_inside(self, other_shape):
        return (self.width // other_shape.width) * (self.height // other_shape.height)

class Square(Rectangle):
    def __init__(self, input_side: float) -> None:
        super().__init__(input_side, input_side)

#    def __init__(self, input_width: float, input_height: float) -> None:
#         self.width = input_width
#         self.height = input_height

    def set_side(self, input_side: float):
        self.width = input_side
        self.height = input_side

rectangle_A = Rectangle(3, 4)
print(rectangle_A.get_area()) #12
print(rectangle_A.get_perimeter()) #14
print(rectangle_A.get_diagonal()) #5
rectangle_A.get_picture()

rectangle_B = Rectangle(4, 1)
print(rectangle_A.get_amount_inside(rectangle_B)) #0

rectangle_A.set_width(10) #width changed to 10
print(rectangle_A.get_area()) #10 * 4 = 40

square_A = Square(5)
print(square_A.get_area()) #25
print(str(square_A))