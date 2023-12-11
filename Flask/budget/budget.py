from datetime import datetime


class Entry:
    def __init__(self, amount_type, amount):
        self.amount_type = amount_type
        self.amount = amount

    def __str__(self):
        return f"{self.amount_type}:  {self.amount}"


class IncomeEntry(Entry):
    def __init__(self, amount_type, amount, sender, additional_info, date=datetime.now()):
        super().__init__(amount_type, amount)
        self.sender = sender
        self.additional_info = additional_info
        self.date = datetime.strptime(str(date)[0:19], "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.amount_type}:  {self.amount}, {self.sender}, {self.additional_info}, {self.date}"


class ExpensesEntry(Entry):
    def __init__(self, amount_type, amount, payment_option, received_good_or_service, date=datetime.now()):
        super().__init__(amount_type, amount)
        self.payment_option = payment_option
        self.received_good_or_service = received_good_or_service
        self.date = datetime.strptime(str(date)[0:19], "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.amount_type}:  {self.amount}, {self.payment_option}, {self.received_good_or_service}, {self.date}"


class Budget:
    def __init__(self):
        self.summary = []

    def enter_income(self, amount, sender, additional_info):
        amount = float(amount)
        self.summary.append(IncomeEntry("Income", amount, sender, additional_info))

    def enter_expense(self, amount, payment_option, received_good_or_service):
        amount = float(amount)
        self.summary.append(ExpensesEntry("Expense", amount, payment_option, received_good_or_service))

    def get_balance(self):
        income = 0.0
        expense = 0.0
        for entry in self.summary:
            if isinstance(entry, IncomeEntry):
                income += entry.amount
            elif isinstance(entry, ExpensesEntry):
                expense += entry.amount

        return income - expense

    def get_report(self):
        for entry in self.summary:
            if isinstance(entry, IncomeEntry):
                return f"Income: {entry.amount} Sender: {entry.sender} Additional info: {entry.additional_info} Entry date: {entry.date}"
            elif isinstance(entry, ExpensesEntry):
                return f"Expenses: {entry.amount} Payment option: {entry.payment_option}, Received good or service: {entry.received_good_or_service} Entry date: {entry.date}"




def printRed(skk):
    print(f"\033[91m {skk}\033[00m")


def printGreen(skk):
    print(f"\033[92m {skk}\033[00m")