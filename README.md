Project Description:
This project is to practice utilizing classes in Python. This budget app will will have a `Category` class that will have methods for that category such as `deposit`, `withdrawl`, `get_balance`, `transfer`, and `check_funds`. You will be able to "print" a category to see the transactions for that category and the total remaining for the category.

Additionally, there will be a `create_spend_chart` function that will create a bar chart showing how much spending has been done in each category. It will look somthing like this:

Percentage spent by category
100|  
 90|  
 80|  
 70|  
 60| o  
 50| o  
 40| o  
 30| o  
 20| o o  
 10| o o o  
 0| o o o

---

F C A  
 o l u  
 o o t  
 d t o  
 h  
 i  
 n  
 g
^prettier keeps messing this up

Updates:
Added functions for deposits, withdrawal, and get_balance.
Added function for transfers between categories. All FCC tests for deposits, withdrawal, and transfers pass.
Added check balance function (I should have finished this function before the withdrawal and deposit functions, but whatever). All the budget functions now work. Now I just need to work on how the instances and the overall budget print to the console. That will be for tomorrow.
I took a couple of days off to work on some VBA for work, but back to it today
Added `print_category` which correctly prints each category to the console. All tests pass except the bar chart which I will begin work on now.
Added `create_spend_chart` function along with helper functions `_get_cat_total` and `_get_total`. Together, these calculate the percentage of spending for each category.
The math appears to work, not on to the visual.

Started on the visual. The top portion mostly works, but it's a bit hacky. It also has a couple of items that need to be fixed, namely:
complete-Add an extra line to he percentage markers to account for the "0%" in the required output
complete-Draw the sumline based on the width of the graph

Sumline added
Category names added
One math error seems to remain. I believe it is related to how FCC expects the category graph to round. Will fix it once I get an answer on what it expects. Once that is sqashed, this app is done.

Solved the graph error. There is one error that still causes the test not to pass (I think it is an extra and or missing space). Everything else works. The graph was off slightly b/c I rounded to 1 rather than 2 decimal places when determining if a circle would be drawn. Almost done.
