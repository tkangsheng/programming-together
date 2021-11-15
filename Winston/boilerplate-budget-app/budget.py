from typing import final


class Category:
    WIDTH_OF_LEDGER = 30

    def __init__(self, title : str) -> None:
        self.title = title
        self.currentAmount : float = 0
        self.ledger : list = []

    def deposit(self, amount : float, description : str = ''):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.currentAmount += amount

    def withdraw(self, amount : float, description : str = ''):
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
        if self.withdraw(amount, f'Transfer to {another_category.title}'):
            another_category.deposit(amount, f"Transfer from {self.title}")
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
        return (Category.WIDTH_OF_LEDGER - len(self.title)) // 2

    def items_in_ledger(self):
        lines_of_ledger = []
        for item in self.ledger:
            description = item["description"][:23]
            amount = '%.2f' % item["amount"]
            whitespaces = ' ' * (Category.WIDTH_OF_LEDGER - len(description) - len(amount))
            lines_of_ledger.append(f'{description}{whitespaces}{amount}')
        return '\n'.join(lines_of_ledger)

    def total_amount(self):
        formatted_amount = '%.2f' % self.currentAmount
        return f'Total: {formatted_amount}'


def create_spend_chart(categories : list):
    final_str = ''

    # calculate percentages
    # calculate width of the chart
    # calculate height of the chart
    return final_str

clothing = Category("Clothing")
clothing.deposit(232, 'Adidas Ultraboost')
clothing.deposit(30, 'Couple T-shirt')

gaming = Category('Gaming')
gaming.deposit(300, 'Maplestory Credits')

food = Category("Food")
title_bar = food.title_bar()
food.deposit(-12, 'Chicken McNuggets x20')
food.deposit(-12, 'Chicken McNuggets x20')
food.deposit(-12, 'Chicken McNuggets x20')
food.deposit(-12, 'Chicken McNuggets x20')
food.deposit(-12, 'Chicken McNuggets x20')

categories = [clothing, gaming, food]

create_spend_chart(categories)