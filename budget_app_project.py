#Creates the budget category class and class methods
class Category:
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.description = ""
        self.ledger = []

    #When printing the category, prints the list of category transactions.
    def __str__(self):
        return f'{self.print_category(self.category)}'

    #Adds ledger entry for deposit with amount and optional description
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
    #Adds ledger entry for withdrawal with amount and optional description
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            amount = amount * -1
            self.ledger.append({'amount': amount, 'description': description})
            return True
        else:
            return False     
    #Returns current balance of category.
    def get_balance(self):
        bal = 0
        i = 0
        for item in self.ledger:
            amount = self.ledger[i]["amount"]
            bal = bal + amount
            i += 1
        return bal
    #Adds ledger entry for each category with deposit/withdrawal amount and description of where the transfer came from/to
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            description = 'Transfer to ' + other_category.category
            self.withdraw(amount, description)
            description = 'Transfer from ' + self.category
            other_category.deposit(amount, description)
            return True
        else: return False
    # Accepts an amount as an argument to see if there are sufficient funds for a transaction
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    #creates a list of the transactions in the category beneath the category name with asterisks filling up to 30 total characters and the category's current balance
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
            size = len(f'{self.ledger[index]["description"][:23]}{self.ledger[index]["amount"]:.2f}')
            spaces = ""
            x = 0
            while x < 30 - size:
                spaces = spaces + " "
                x += 1
            ret_string = ret_string + f'{self.ledger[index]["description"][:23]}{spaces}{self.ledger[index]["amount"]:.2f}\n'   
        total = f'Total: {self.get_balance():.2f}'
        return f'{title}\n{ret_string}{total}'

#Creates a chart to show the distribution of spending as a percentage of total spent
def create_spend_chart(categories):
    total = _get_total(categories)
    cat_totals = []
    sumline= _make_sum_line(categories)
    i = 0
    #creates a tuple of the category name and a string of os with each o representing 10% of total spending rounded down to the nearest 10%.
    while i < len(categories):
        cat_totals.append((categories[i].category, _make_circles(round(_get_cat_total(categories[i])/total,2))))
        i += 1
    names = _make_category_names(categories)
    sa = []
    ss = " "
    j = 0
    #iterates through each category string of " " and "o" stored in cat_totals to place create an array (sa) of strings (ss). Each item of the category strings are separated by 2 spaces. These are then used to return the graph line by line in the return statement, so sa[0] would return the first ss string containing either " " or "o" for the category followed by two spaces between each.
    while j <= 10:
        for item in cat_totals:
            ss = ss + item[1][j] + "  "
        sa.append(ss)
        ss = " "
        j += 1
    return(f'Percentage spent by category\n100|{sa[0]}\n 90|{sa[1]}\n 80|{sa[2]}\n 70|{sa[3]}\n 60|{sa[4]}\n 50|{sa[5]}\n 40|{sa[6]}\n 30|{sa[7]}\n 20|{sa[8]}\n 10|{sa[9]}\n  0|{sa[10]}\n{sumline}\n{names}')

#Generates a sum of all the spending transactions in a category
def _get_cat_total(category):
    spending_sum = 0
    i = 0
    while i < len(category.ledger):
        if category.ledger[i]['amount'] < 0:
            spending_sum = spending_sum + round(category.ledger[i]['amount'],2)
            i += 1
        else:
            i +=1
    return round(spending_sum,2)

#Generates a sting of " " and "o". Each circle represents 10% or more in spending for a category against the total spending. All categories will have a "o" for 0%, to the string is 11 characters long.
def _make_circles(percent):
    circle_number = percent * 10
    circle = ""
    i = 10
    while i >= 0:
        if i > circle_number:
            circle = circle + " "
        else:
            circle = circle + "o"
        i -= 1
    return circle

#Generates a sum of all spending in all categories to be used to determin percentage of spending in each category
def _get_total(categories):
    total = 0
    i = 0
    while i < len(categories):
        total = total + _get_cat_total(categories[i])
        i += 1
    return round(total,2)

#Generates the X-axis for the spending chart that extends two spaces past the final bar
def _make_sum_line(categories):
    sumline = "    -"
    i = 1
    while i <= len(categories):
        sumline = sumline + "---"
        i += 1
    sumline = sumline + ""
    return sumline

#Similar to the impletmentation of the circles above. Iterates over each name and adds the letter at the current index to a string. The string will print the category names vertically with two spaces between each letter. The string does not have an enter at the end.
def _make_category_names(categories):
    name_list = []
    for name in categories:
        name_list.append(name.category)
    max_length = (len(max(name_list, key = len)))
    test = "     "
    out = []
    i = 0
    while i < max_length:
        for name in name_list:
            if i >= len(name):
                test = test + "   "
            else:
                test = test + name[i] + "  "
        out.append(test)
        i += 1
        test = "     "
    return_string = ""
    for num, index in enumerate(out):
        if num == len(out)-1:
            return_string = return_string + index
        else:
            return_string = return_string + index + "\n"
    return return_string

#Test categories and transactions:
pets = Category("Pets")
food = Category("Food")
clothing = Category('Clothing')
automobile = Category('Automobile')
gifts = Category('Gifts')
business = Category('Business')
entertainment = Category('Entertainment')

pets.deposit(1000.01,"initial deposit")
pets.withdraw(10,"dog food")
pets.withdraw(58,"cat litter")
food.deposit(400,"initial deposit")
food.withdraw(440,"cake")
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing.deposit(150, "initial deposit")
clothing.withdraw(75.00, 'shirt')
clothing.withdraw(20.25, 'pants')
automobile.deposit(1200, "initial deposit")
automobile.withdraw(75.54, 'car payment')
automobile.withdraw(47.83, 'gas')
automobile.transfer(50.50, food)
food.transfer(100, clothing)
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(food)
the_list = (food, pets, clothing, automobile, gifts, business, entertainment)
print(create_spend_chart(the_list))
