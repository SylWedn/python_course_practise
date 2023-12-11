# -----------------------------------------------
# P.5.5
# -----------------------
# • Create a "Budget" program which would:
#   • Let a user input their income.
#   • Let a user input their expenses.
#   • Show the user their Income Statement (the statement that shows the user's
#     income and expenditures, and also shows whether a user is making profit or
#     loss for a given period).
#   • Show the user their Income and Expenditure Account (the detailed summary
#     of every income and expense, with their type and amount).
#   • Let the user exit the program.
#
# Recommendation on how it could be done:
#   • The program could have a class Entry with attributes money_type (income
#     or expenses) and amount. It could also have a str() method which would
#     return how the object should be printed.
#   • The program could have a class Budget with the attribute log and the
#     following methods:
#     1. init() - it would initialize a log attribute (empty at the beginning)
#        in which the created income and expenses objects could be placed.
#     2. add_income_entry(self, amount) - it would get the amount as an input,
#        create an income object and put it in a budget log.
#     3. add_expenses_entry(self, amount) - it would get the amount as an
#        input, create an expenses object and put it in a budget log.
#     4. print_income_statement(self) - to print the Income Statement.
#     5. print_ie_account(self) - to print the Income and Expenditure Account.
# -----------------------------------------------

class Entry:

    def __init__(self, money_type, amount):
        self.money_type = money_type
        self.amount = amount

    def __str__(self):
        return f"{self.money_type}: {self.amount}"


class Budget:

    def __init__(self):
        self.log = []

    def add_income_entry(self, income):
        entry = Entry('Income', income)
        self.log.append(entry)

    def add_expenses_entry(self, expenses):
        entry = Entry('Expenses', expenses)
        self.log.append(entry)

    def print_income_statement(self):
        total_income = sum(entry.amount for entry in self.log if entry.money_type == "Income")
        total_expenses = sum(entry.amount for entry in self.log if entry.money_type == "Expenses")
        profit_loss = total_income - total_expenses
        print(f'Income statement: \nTotal income: {total_income} \nTotal expenses: {total_expenses}')
        if profit_loss > 0:
            print('You are making profit')
        elif profit_loss < 0:
            print('You are making loss')

    def print_ie_account(self):
        for entry in self.log:
            print(entry)


budget = Budget()

while True:
    try:
        user_input = int(input(
            "\nEnter '1' to enter income."
            "\nEnter '2' to enter expenses."
            "\nEnter '3' to print the income statement."
            "\nEnter '4' to print income and expenses account."
            "\nEnter '5' to end the program: "
        ))

        if user_input == 1:
            income = round(float(input("Enter your income: ")), 2)
            budget.add_income_entry(income)
        elif user_input == 2:
            expenses = round(float(input("Enter your expenses: ")), 2)
            budget.add_expenses_entry(expenses)
        elif user_input == 3:
            budget.print_income_statement()
        elif user_input == 4:
            budget.print_ie_account()
        elif user_input == 5:
            print("=============================================")
            print("End")
            break
        else:
            print("Error: Invalid action!")

    except ValueError:
        print("Error: Invalid action!")


