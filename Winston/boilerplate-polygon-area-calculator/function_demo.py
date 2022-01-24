class Cookie:
    sugar : int
    butter : int
    def __init__(self, sugar, butter) -> None:
        self.sugar = sugar
        self.butter = butter

    def bake(self):
        print(f'cookie baked with {self.sugar}g sugar')


low_sugar_cookie = Cookie(10, 1)
high_sugar_cookie = Cookie(100, 1)

high_sugar_cookie.bake()