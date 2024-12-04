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

    def print_category(self):
        stars = (30 - len(self.category)) // 2
        star_line = ""
        i = 0
        while i < stars:
            star_line = star_line + "*"
            i += 1
        if len(f'{star_line}{self}{star_line}') != 30:
            print(f'{star_line}{self}{star_line}*')

        else:
            print(f'{star_line}{self}{star_line}')
        
        for index in range(len(self.ledger)):
            # for key in self.ledger[index]:
            skippy = len(f'{self.ledger[index]["description"][:23]}{self.ledger[index]["amount"]:.2f}')
            spaces = ""
            x = 0
            while x < 30 - skippy:
                spaces = spaces + " "
                x += 1

            print(f'{self.ledger[index]["description"][:23]}{spaces}{self.ledger[index]["amount"]:.2f}')
            # spaces = ""
            # j = 
            # while j < 30:
            #     spaces = spaces + " "
            #     j += 1
        
        # print(f'{self.ledger[0]["description"][:23]}{self.ledger[0]["amount"]:.2f}')


def create_spend_chart(categories):
    pass

# A title line of 30 characters where the name of the category is centered in a line of \* characters.
# A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
# A line displaying the category total.

# Here is an example of the output:

# *************Food*************
# initial deposit 1000.00
# groceries -10.15
# restaurant and more foo -15.89
# Transfer to Clothing -50.00
# Total: 923.96








































pets = Category("Pets")
food = Category("Food")

pets.deposit(1000.01,"initial deposit")
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
pets.print_category()
clothing.print_category()



