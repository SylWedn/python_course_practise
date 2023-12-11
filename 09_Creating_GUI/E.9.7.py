import tkinter as tk
from tkinter import messagebox

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
        account_text = "IE Account:\n"
        for entry in self.log:
            if isinstance(entry, IncomeEntry):
                account_text += f"Income: {entry}\n"
            elif isinstance(entry, ExpensesEntry):
                account_text += f"Expenses: {entry}\n"
        return account_text

    def print_income_statement(self):
        total_income = sum(entry.amount for entry in self.log if isinstance(entry, IncomeEntry))
        total_expenses = sum(entry.amount for entry in self.log if isinstance(entry, ExpensesEntry))
        profit_loss = total_income - total_expenses
        statement_text = f"Income statement:\n" \
                         f"Total income: {total_income}\n" \
                         f"Total expenses: {total_expenses}\n"
        if profit_loss > 0:
            statement_text += "You are making profit"
        elif profit_loss < 0:
            statement_text += "You are making loss"
        return statement_text


def handle_income_entry():
    try:
        income = round(float(income_entry.get()), 2)
        sender = sender_entry.get()
        additional_info = additional_info_entry.get()
        budget.add_income_entry(income, sender, additional_info)
        messagebox.showinfo("Success", "Income entry added successfully!")
        income_entry.delete(0, tk.END)
        sender_entry.delete(0, tk.END)
        additional_info_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid amount.")


def handle_expenses_entry():
    try:
        expenses = round(float(expenses_entry.get()), 2)
        payment_option = payment_option_entry.get()
        received_good_or_service = received_good_or_service_entry.get()
        budget.add_expenses_entry(expenses, payment_option, received_good_or_service)
        messagebox.showinfo("Success", "Expenses entry added successfully!")
        expenses_entry.delete(0, tk.END)
        payment_option_entry.delete(0, tk.END)
        received_good_or_service_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid amount.")


def print_income_statement():
    statement_text = budget.print_income_statement()
    messagebox.showinfo("Income Statement", statement_text)


def print_ie_account():
    account_text = budget.print_ie_account()
    messagebox.showinfo("Income and Expenses Account", account_text)


budget = Budget()

window = tk.Tk()
window.title("Budget Tracker")

income_label = tk.Label(window, text="Income")
income_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

income_entry = tk.Entry(window)
income_entry.grid(row=0, column=1, padx=10, pady=5)

sender_label = tk.Label(window, text="Sender")
sender_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

sender_entry = tk.Entry(window)
sender_entry.grid(row=1, column=1, padx=10, pady=5)

additional_info_label = tk.Label(window, text="Additional Info")
additional_info_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

additional_info_entry = tk.Entry(window)
additional_info_entry.grid(row=2, column=1, padx=10, pady=5)

income_button = tk.Button(window, text="Add Income Entry", command=handle_income_entry)
income_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

expenses_label = tk.Label(window, text="Expenses")
expenses_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

expenses_entry = tk.Entry(window)
expenses_entry.grid(row=4, column=1, padx=10, pady=5)

payment_option_label = tk.Label(window, text="Payment Option")
payment_option_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

payment_option_entry = tk.Entry(window)
payment_option_entry.grid(row=5, column=1, padx=10, pady=5)

received_good_or_service_label = tk.Label(window, text="Received Goods/Services")
received_good_or_service_label.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)

received_good_or_service_entry = tk.Entry(window)
received_good_or_service_entry.grid(row=6, column=1, padx=10, pady=5)

expenses_button = tk.Button(window, text="Add Expenses Entry", command=handle_expenses_entry)
expenses_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

print_income_statement_button = tk.Button(window, text="Print Income Statement", command=print_income_statement)
print_income_statement_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

print_ie_account_button = tk.Button(window, text="Print Income and Expenses Account", command=print_ie_account)
print_ie_account_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()