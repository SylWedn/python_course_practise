import pickle
from income_entry import IncomeEntry
from expenses_entry import ExpensesEntry


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
            print(entry)

            if isinstance(entry, IncomeEntry):
                print('Income:', entry.amount, 'Sender:', entry.sender, 'Additional info:', entry.additional_info)
            elif isinstance(entry, ExpensesEntry):
               print('Expenses:', entry.amount, 'Payment option:', entry.payment_option, 'Received good or service:', entry.received_good_or_service)

    def print_income_statement(self):
        total_income = sum(entry.amount for entry in self.log if isinstance(entry, IncomeEntry))
        total_expenses = sum(entry.amount for entry in self.log if isinstance(entry, ExpensesEntry))
        profit_loss = total_income - total_expenses
        print(f'Income statement: \nTotal income: {total_income} \nTotal expenses: {total_expenses}')
        if profit_loss > 0:
            print("You are making profit")
        elif profit_loss < 0:
            print("You are making loss")

    def save_to_file(self):
        with open('budget.pkl', 'wb') as pickle_out:
            pickle.dump(self.log, pickle_out)

    def extract_from_file(self):
        with open('budget.pkl', 'rb') as pickle_in:
            self.log = pickle.load(pickle_in)

