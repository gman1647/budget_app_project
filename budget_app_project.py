class Category:
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.description = ""
        self.ledger = []

    def __str__(self):
        #return f'{self.category}'
        # category = self.category
        # print(category)
        return f'{self.print_category(self.category)}'

    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            amount = amount * -1
            self.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False     

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
        if self.check_funds(amount):
            description = 'Transfer to ' + other_category.category
            self.withdraw(amount, description)
            description = 'Transfer from ' + self.category
            other_category.deposit(amount, description)
            return True
        else: return False
    # A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def print_category(self, name):
        stars = (30 - len(self.category)) // 2
        star_line = ""
        title = ""
        i = 0
        while i < stars:
            star_line = star_line + "*"
            i += 1
        if len(f'{star_line}{name}{star_line}') != 30:
            title = f'{star_line}{name}{star_line}*'

        else:
            title = f'{star_line}{name}{star_line}'
        ret_string = ""
        for index in range(len(self.ledger)):
            skippy = len(f'{self.ledger[index]["description"][:23]}{self.ledger[index]["amount"]:.2f}')
            spaces = ""
            x = 0
            while x < 30 - skippy:
                spaces = spaces + " "
                x += 1
            ret_string = ret_string + f'{self.ledger[index]["description"][:23]}{spaces}{self.ledger[index]["amount"]:.2f}\n'   
        total = f'Total: {self.get_balance():.2f}'
        
        return f'{title}\n{ret_string}{total}'

def create_spend_chart(categories):
    pass

pets = Category("Pets")
food = Category("Food")
clothing = Category('Clothing')

pets.deposit(1000.01,"initial deposit")
pets.withdraw(10,"dog food")
pets.withdraw(58,"cat litter")
food.deposit(400,"initial deposit")
food.withdraw(440,"cake")
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')


# print(f'current pet balance is:  {pets.get_balance()}')
# print(f'current food balance is:  {food.get_balance()}')
# print(f'current clothing balance is: {clothing.get_balance()}')

food.transfer(100, clothing)

# print(f'current food balance is:  {food.get_balance()}')
# print(f'current clothing balance is: {clothing.get_balance()}')

# print(f'This is the food ledger: {food.ledger}')
# print(f'This is the clothing ledger: {clothing.ledger}')

print(food)
print(clothing)
print(pets)

