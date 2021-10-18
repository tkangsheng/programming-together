class Category:

    def __init__(self, title : str) -> None:
        self.title = title
        self.currentAmount : float = 0
        self.ledger : list = []

    def deposit(self, amount : float, description = ''):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.currentAmount += amount

    def withdraw(self, amount : float, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            self.currentAmount -= amount
            return True
        return False

    def get_balance(self):
        return self.currentAmount

    def transfer(self, amount : float, another_category):
        if self.withdraw(amount, "Transfer to [Destination Budget Category]"):
            another_category.deposit(amount, "Transfer from [Source Budget Category]")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.currentAmount

    def __str__(self) -> str:
        return f'{self.title_bar()}\n{self.items_in_ledger()}\n{self.total_amount()}'

    def title_bar(self):
        if len(self.title) % 2 == 0:
            return '*'*self.number_of_stars() + self.title + '*'*self.number_of_stars()
        else:
            return '*'*self.number_of_stars() + self.title + '*'*(self.number_of_stars() + 1)

    def number_of_stars(self) -> int:
        return (30 - len(self.title)) // 2

    def items_in_ledger(self):
        return ''

    def total_amount(self):
        return f'Total: {self.currentAmount}'


def create_spend_chart(categories):
    return


money = Category("Food")
title_bar = money.title_bar()
print(title_bar)
print(len(title_bar))
# a = Category("food")
# a.deposit(100)
# successful = a.withdraw(23.4)
# amount = a.get_balance()
# a.check_funds(101)
# print(a)