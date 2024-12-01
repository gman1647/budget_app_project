class Category:
    def __init__(self, category,):
        self.category = category
        self.amount = 0
        self.description = ""
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

#{'amount': amount, 'description': description}
    def withdraw(self):
        pass

    def get_balance(self):
        pass
    
    def transfer(self, amount, other_category):
        pass
    
    def check_funds(self, amount):
        pass

def create_spend_chart(categories):
    pass

my_instance = Category("Pets")

print(my_instance.ledger)
my_instance.deposit(10)
print(my_instance.ledger)
print(my_instance.ledger[0])