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

# takes a list of categories as an argument. It should return a string that is a bar chart.

# The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

# This function will be tested with up to four categories.

# Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

#FCC Forum seems to think this is a percentage of the total expendature
def create_spend_chart(categories):
    print(f'\nPercentage Spent per Category')
    total = _get_total(categories)
    cat_totals = []
    sumline= _make_sum_line(categories)
    i = 0
    while i < len(categories):
        cat_totals.append((categories[i].category, _make_circles(round(_get_cat_total(categories[i])/total,1))))
        i += 1
    names = _make_category_names(categories)# print(cat_totals)
    # print(cat_totals[0][1][10])
    sa = []
    ss = " "
    j = 0
    while j <= 10:
        for item in cat_totals:
            ss = ss + item[1][j] + "  "
        sa.append(ss)
        ss = " "
        j += 1

    # item_test = cat_totals[0]
    # item_test2 = cat_totals[1]
    # print(item_test)
    # name_test = item_test[0]
    # name_test2 = item_test2[0]
    # print(name_test)
    # circle_number = item_test[1] * 10
    # print(int(circle_number))
    # circle = "O"
    # i=0
    # while i < int(circle_number):
    #     circle = circle + "O"
    #     i += 1
    # print(circle)
    print(f'100|{sa[0]}\n 90|{sa[1]}\n 80|{sa[2]}\n 70|{sa[3]}\n 60|{sa[4]}\n 50|{sa[5]}\n 40|{sa[6]}\n 30|{sa[7]}\n 20|{sa[8]}\n 10|{sa[9]}\n  0|{sa[10]}\n{sumline}\n{names}')
    # {name_test[0]}   {name_test2[0]}\n     {name_test[1]}   {name_test2[1]}\n     {name_test[2]}   {name_test2[2]}\n     {name_test[3]}   {name_test2[3]}')

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

def _make_circles(percent):
    circle_number = percent
    circle = ""
    i = 1
    while i >= 0:
        if i >= circle_number:
            circle = circle + " "
        else:
            circle = circle + "o"
        i -= .1
    return circle

def _get_total(categories):
    total = 0
    i = 0
    while i < len(categories):
        total = total + _get_cat_total(categories[i])
        i += 1
    return round(total,2)

def _make_sum_line(categories):
    sumline = "    "
    i = 0
    while i < len(categories):
        sumline = sumline + "--"
        i += 1
    sumline = sumline + "----"
    return sumline

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
    for index in out:
        return_string = return_string + index + "\n"
    return return_string




    # print(test)


pets = Category("Pets")
food = Category("Food")
clothing = Category('Clothing')
automobile = Category('Automobile')

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

# print(f'current pet balance is:  {pets.get_balance()}')
# print(f'current food balance is:  {food.get_balance()}')
# print(f'current clothing balance is: {clothing.get_balance()}')

food.transfer(100, clothing)

# print(f'current food balance is:  {food.get_balance()}')
# print(f'current clothing balance is: {clothing.get_balance()}')

# print(f'This is the food ledger: {food.ledger}')
# print(f'This is the clothing ledger: {clothing.ledger}')

# print(food)
# print(clothing)
# print(pets)

# print(_get_total(food))
# print(_get_total(pets))
# print(_get_total(clothing))
print(automobile)

the_list = (food, pets, clothing, automobile)
create_spend_chart(the_list)

# _make_category_names(the_list)
