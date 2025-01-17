MAX_PERCENT = 100
PERCENT_DENOMINATION = 10

class Category:
    WIDTH_OF_LEDGER = 30

    def __init__(self, title: str):
        self.title: str = title
        self.currentAmount: float = 0
        self.ledger: list = []

    def deposit(self, amount: float, description: str = ''):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.currentAmount += amount

    def withdraw(self, amount: float, description: str = '') -> bool:
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            self.currentAmount -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.currentAmount

    def transfer(self, amount: float, another_category) -> bool:
        if self.withdraw(amount, f'Transfer to {another_category.title}'):
            another_category.deposit(amount, f"Transfer from {self.title}")
            return True
        return False

    def check_funds(self, amount) -> bool:
        return amount <= self.currentAmount

    def __str__(self) -> str:
        return f'{self.title_bar()}\n{self.items_in_ledger()}\n{self.total_amount()}'

    def title_bar(self) -> str:
        if len(self.title) % 2 == 0:
            return '*'*self.number_of_stars() + self.title + '*'*self.number_of_stars()
        else:
            return '*'*self.number_of_stars() + self.title + '*'*(self.number_of_stars() + 1)

    def number_of_stars(self) -> int:
        return (Category.WIDTH_OF_LEDGER - len(self.title)) // 2

    def items_in_ledger(self) -> str:
        lines_of_ledger = []
        for item in self.ledger:
            description = item["description"][:23]
            amount = '%.2f' % item["amount"]
            whitespaces = ' ' * (Category.WIDTH_OF_LEDGER -
                                 len(description) - len(amount))
            lines_of_ledger.append(f'{description}{whitespaces}{amount}')
        return '\n'.join(lines_of_ledger)

    def total_amount(self) -> str:
        formatted_amount = '%.2f' % self.currentAmount
        return f'Total: {formatted_amount}'

def format_percent(percent: int) -> str:
    whitespace_count = len(str(MAX_PERCENT)) - len(str(percent))
    whitespace = ' ' * whitespace_count
    return f'{whitespace}{percent}| '

def calculate_total_balance(categories: list[Category]) -> float:
    total_balance = 0
    for category in categories:
        withdrawal = get_withdrawal_total(category)
        total_balance += withdrawal
    return total_balance

def get_withdrawal_total(category: Category) -> float:
    withdrawal_total = 0
    for item in category.ledger:
        amount = item['amount']
        if amount < 0:  # withdrawal
            withdrawal_total += -amount
    return withdrawal_total

def create_dots(category: Category, size_of_categories: int, total_balance: float, chart_percent: int) -> str:
    category_balance = get_withdrawal_total(category)
    if total_balance == 0:
        category_percent = (1 / size_of_categories) * 100
    else:
        category_percent = (category_balance / total_balance) * 100

    if category_percent >= chart_percent:
        return 'o  '
    else:
        return '   '

def get_max_title_length(categories: list[Category]) -> int:
    max_length = 0;
    for category in categories:
        current_length = len(category.title)
        if current_length > max_length:
            max_length = current_length

    return max_length

def create_spend_chart(categories: list[Category]):
    # calculate percentages
    # calculate width of the chart
    # calculate height of the chart
    HEADER = 'Percentage spent by category'
    END_OF_LINE = '\n'
    Y_LABEL_SIZE = 4 # len('100|')
    chart_percent = MAX_PERCENT
    total_balance = calculate_total_balance(categories)
    size_of_categories = len(categories)
    all_lines = [ HEADER ]

    # create percent lines
    while chart_percent >= 0:
        percent_label = format_percent(chart_percent)

        all_category_dots = []
        for category in categories:
            category_dots = create_dots(category, size_of_categories, total_balance, chart_percent)
            all_category_dots.append(category_dots)
        percent_line = f'{percent_label}{"".join(all_category_dots)}'
        all_lines.append(percent_line)
        chart_percent -= PERCENT_DENOMINATION

    # create border
    border = ' ' * Y_LABEL_SIZE + '-'*(len(categories)*3 + 1)
    all_lines.append(border)

    # create category label lines
    size_of_the_longest_title = get_max_title_length(categories)
    for letter_index in range(size_of_the_longest_title):
        all_categories_letter_in_this_index : list[str] = []
        for category in categories:
            category_title_letter : str
            if letter_index < len(category.title):
                category_title_letter = category.title[letter_index]
            else:
                category_title_letter = ' '
            letter_block = category_title_letter + ' '*2
            all_categories_letter_in_this_index.append(letter_block)
        line = ' ' * (Y_LABEL_SIZE + 1) + "".join(all_categories_letter_in_this_index)
        all_lines.append(line)
    return END_OF_LINE.join(all_lines)

