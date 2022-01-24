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
        SIZE_LIMIT = 50
        if (self.height > SIZE_LIMIT or self.width > SIZE_LIMIT):
            print("Too big for picture.")

        lines = []
        for i in range(self.height):
            lines.append('*'*self.width)
        return '\n'.join(lines)

    def get_amount_inside(self, otherRectangle):
        # what's a quick way to determine if a rectangle can fit inside another rectangle?
        # what are the different cases for fitting 1 rectangle into another?
        # case 1:
        # the width and height of otherRectangle is bigger than self -> 0
        # case 2:
        # the width of otherRectangle is bigger than self.width -> 0
        # case 3:
        # the height of otherRectangle is bigger than self.height -> 0
        # case 4:
        # the width and height are both within self.width. then otherRectangle.width * N == self.width. and otherRectangle.height * M == self.height where N is the number of otherRectangle u can fit side-to-side in self, and M is the number of otherRectangle u can fit on top of each other in self.
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
picture = shapeA.get_picture()
print(picture)