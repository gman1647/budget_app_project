class Category:
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.description = ""
        self.ledger = []

    def __str__(self):
        return f'{self.category}'
    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if amount > self.get_balance():
            return False
        else:
            amount = amount * -1
            self.ledger.append({'amount': amount, 'description': description}) 
            return True     

    def get_balance(self):
        bal = 0
        i = 0
        for item in self.ledger:
            amount = self.ledger[i]["amount"]
            bal = bal + amount
            i += 1
        return bal
        #Could I use enumarate to do this?

    def transfer(self, amount, other_category):
        if amount > self.get_balance():
            return False
        else:
            description = 'Transfer to ' + other_category.category
            self.withdraw(amount, description)
            description = 'Transfer from ' + self.category
            other_category.deposit(amount, description)
            return True
    
    def check_funds(self, amount):
        pass


def create_spend_chart(categories):
    pass

pets = Category("Pets")
food = Category("Food")

pets.deposit(1000,"initial deposit")
pets.withdraw(10,"dog food")
pets.withdraw(58,"cat litter")
food.deposit(400,"initial deposit")
food.withdraw(440,"cake")
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')

print(f'current pet balance is:  {pets.get_balance()}')
print(f'current food balance is:  {food.get_balance()}')
print(f'current clothing balance is: {clothing.get_balance()}')

food.transfer(100, clothing)

print(f'current food balance is:  {food.get_balance()}')
print(f'current clothing balance is: {clothing.get_balance()}')

print(f'This is the food ledger: {food.ledger}')
print(f'This is the clothing ledger: {clothing.ledger}')




