class Category:
    current_amount : float = 0
    ledger : list = []

    def deposit(self, amount : float, description = '')
        self.ledger.append({
            "amount" : amount, 
            "description" : description
            })
        self.current_amount += amount
    
    def withdraw(self, amount : float, description = '')
        if self.current_amount >= amount:
            self.ledger.append({
                "amount" : amount, 
               "description" : description
                })
            self.currentAmount += amount
            return True
        else:
            return False

    def get_balance(self):
        return current_amount

    def transfer(self, amount : float, another_category : Category):

    
    def check_funds(self, amount):
        return self.current_amount >= amount

    def __str__(self):
        len(self)