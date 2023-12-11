class Entry:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)


class IncomeEntry(Entry):

    def __init__(self, amount, sender, additional_info):
        super().__init__(amount)
        self.sender = sender
        self.additional_info = additional_info


class ExpensesEntry(Entry):
    def __init__(self, amount, payment_option, received_good_or_service):
        super().__init__(amount)
        self.payment_option = payment_option
        self.received_good_or_service = received_good_or_service


class Budget:

    def __init__(self):
        self.log = []

    def add_income_entry(self, income, sender, additional_info):
        entry = IncomeEntry(income, sender, additional_info)
        self.log.append(entry)

    def add_expenses_entry(self, expenses, payment_option, received_good_or_service):
        entry = ExpensesEntry(expenses, payment_option, received_good_or_service)
        self.log.append(entry)

    def print_ie_account(self):
        print("IE Account:")
        for entry in self.log:
            if isinstance(entry, IncomeEntry):
                print('Income:', entry)
            elif isinstance(entry, ExpensesEntry):
                print('Expenses:', entry)

    def print_income_statement(self):
        total_income = sum(entry.amount for entry in self.log if isinstance(entry, IncomeEntry))
        total_expenses = sum(entry.amount for entry in self.log if isinstance(entry, ExpensesEntry))
        profit_loss = total_income - total_expenses
        print(f"Income statement: "
              f"\nTotal income: {total_income} "
              f"\nSender: {sender} "
              f"\nAdditional info: {additional_info}"
              f"\nTotal expenses: {total_expenses} "
              f"\nPayment option: {payment_option} "
              f"\nReceived goods or services: {received_good_or_service}")
        if profit_loss > 0:
            print("You are making profit")
        elif profit_loss < 0:
            print("You are making loss")


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
            sender = str(input('Enter the sender: '))
            additional_info = str(input('Enter more info about the transaction: '))
            print("=============================================")
            budget.add_income_entry(income, sender, additional_info)
        elif user_input == 2:
            expenses = round(float(input("Enter your expenses: ")), 2)
            payment_option = str(input('Enter the payment option: '))
            received_good_or_service = str(input('Enter received goods or services: '))
            print("=============================================")
            budget.add_expenses_entry(expenses, payment_option, received_good_or_service)
        elif user_input == 3:
            print("=============================================")
            budget.print_income_statement()
        elif user_input == 4:
            print("=============================================")
            budget.print_ie_account()
        elif user_input == 5:
            print("=============================================")
            print("End")
            break
        else:
            print("Error: Invalid action!")

    except ValueError:
        print("Error: Invalid action!")