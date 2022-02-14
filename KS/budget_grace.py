class Category:
    width_of_ledger = 30
    def __init__(self, title : str) -> None: #to define your own attributes for this category
        self.title = title #eg of a constructor Category("Food")
        self.currentAmount : float = 0
        self.ledger : list = []

    def deposit(self, amount: float, description = ''): # colon is a __ type, equal is a value
        self.ledger.append({  #key value pairs "amount" and amount
            "amount": amount, 
            "description": description
        })
        self.currentAmount += amount #same as "self.currentAmount = self.currentAmount + amount"

    def withdraw(self, amount: float, description = ''):
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
    
    def transfer(self, amount: float, another_category): #another_category: Category
        if self.withdraw(amount, f'Transfer to {another_category.title}'):
            another_category.deposit(amount, f'Transfer from {self.title}')
            return True
        return False

    def check_funds (self, amount):
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
        lines_of_ledger = []
        for item in self.ledger:
            description = item["description"][:23] #assessing the dictionary using 'dictionary', upto but not including
            amount = '%.2f' % item["amount"] #convert 2dp
            whitespaces = ' ' * (Category.width_of_ledger - len(description) - len(amount))
            lines_of_ledger.append(f'{description}{whitespaces}{amount}')
        return '\n'.join(lines_of_ledger)

    def total_amount(self):
        formatted_amount = '%.2f' % self.currentAmount
        return f'Total: {formatted_amount}'

def format_percent (percent: int) -> str:
    whitespace = ' '* (len('100')-len(str(percent)))
    return whitespace

def calculate_total_balance(categories: list[Category]) -> float:
    total_balance = 0
    for category in categories:
        withdrawal = get_total_withdrawal(category)
        total_balance += withdrawal
    return total_balance

def get_total_withdrawal(category: Category) -> float:
    withdrawal_total = 0
    for item in category.ledger:
            if item['amount'] < 0: #withdrawal 
                withdrawal_total += -item['amount']
    return withdrawal_total

def create_dots(categories: list[Category], total_balance: float, chart_percent: int) -> str:
    category_balance = get_total_withdrawal(Category)
    category_percent = (category_balance/total_balance)
    if category_percent >= chart_percent: #torounddown to the nearest 10
        return 'o  '
    else:
        return '   '

clothing = Category("Clothing")
clothing.deposit(232, 'Adidas Ultraboost')
clothing.deposit(30, 'Couple T-shirt')

gaming = Category('Gaming')
gaming.deposit(300, 'Maplestory Credits')

food = Category("Food")
title_bar = food.title_bar()
food.deposit(-12, 'Chicken McNuggets Meal Upsize')
food.deposit(1, 'fried McNuggets')
food.deposit(12, 'Chicken beehooon')

my_categories = [clothing, gaming, food]
border = ' '*4 + '-'*len(my_categories)*3 + '-'

max_percent = 100
percent_denomination =10
chart_percent = max_percent
total_balance = calculate_total_balance(my_categories)
for number in range(11):
    percent_label = f'{format_percent(chart_percent)}{chart_percent}| '
    all_category_dots = []
    for category in my_categories:
        category_dots = create_dots(category, total_balance, chart_percent)
    percent_line = f'{percent_label}{"".join(all_category_dots)}'
    chart_percent -= percent_denomination

print (border)