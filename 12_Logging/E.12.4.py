"""
* aprasyti ir sukurti "stdout_logger", kurio:
    - rasymo lygis yra "INFO"
    - zinutes deda i stdout "stream"
    - raso i faila "stdout.log"
* aprasyti ir sukurti "stderr_logger", kurio:
    - rasymo lygis yra "WARNING"
    - zinutes deda i stderr "stream"
    - raso i stder.log
* sukurti savo nuoziura klase, kuri:
    - per konstruktoriu paims abu virsuje aprasytus logger'ius
    - tures bent 4 metodus, kurie:
        * 2 is ju rasys i stdout.log (INFO ir DEBUG zinutes)
        * 2 is ju rasys i stderr.log (WARNING, EXCEPTION, CRITICAL)

Pastaba: pasistenkite zinutes sudelioti pagal prasme, t.y.
DEBUG ir INFO turetu buti informacinio pobudzio pranesimai, pvz.
"Baigta skaiciuoti xyz", atitinkamai WARNING ispejimas, pvz.
"Paduotas argumento tipas nera xyz, naudokite tipa zyx." ir panasiai.
"""

# from logging import getLogger, FileHandler, Formatter, StreamHandler, WARNING, DEBUG
# from sys import stdout, stderr
#
# stdout_logger = getLogger('stdout_logger')
# stdout_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
# fh_stdout = FileHandler('stdout.log')
# fh_stdout.setFormatter(stdout_formatter)
# stdout_handler = StreamHandler(stdout)
# stdout_handler.setFormatter(stdout_formatter)
# stdout_logger.addHandler(stdout_handler)
# stdout_logger.addHandler(fh_stdout)
# stdout_logger.setLevel(DEBUG)
#
# stderr_logger = getLogger('stderr_logger')
# stderr_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
# fh_stderr = FileHandler('stderr.log')
# fh_stderr.setFormatter(stderr_formatter)
# stderr_handler = StreamHandler(stderr)
# stderr_handler.setFormatter(stderr_formatter)
# stderr_logger.addHandler(stderr_handler)
# stderr_logger.addHandler(fh_stderr)
# stderr_logger.setLevel(WARNING)
#
#
# class Budget:
#     def __init__(self):
#         self.income = 0
#         self.expenses = 0
#         self.initial_income = 0
#         self.initial_expenses = 0
#
#     def add_income(self, amount):
#         if amount < 0:
#             stderr_logger.exception('Klaida')
#             raise ValueError
#         stdout_logger.info('Info zinute')
#         self.income += amount
#
#     def add_expense(self, amount):
#         if amount < 0:
#             stderr_logger.exception('Klaida')
#             raise ValueError("Expense amount must be a positive number.")
#         stdout_logger.debug('Debug zinute')
#         self.expenses += amount
#
#     def get_balance(self):
#         return self.income - self.expenses
#
#     def reset_budget(self):
#         self.income = self.initial_income
#         self.expenses = self.initial_expenses
#
#
#
# # Example usage:
# my_budget = Budget()
# my_budget.add_income(-2000)
# my_budget.add_expense(-1000)
# my_budget.add_income(500)
# my_budget.add_expense(300)
# print("Current Balance:", my_budget.get_balance())  # Output: 1200
#
# my_budget.reset_budget()
# print("Balance after reset:", my_budget.get_balance())

# from logging import getLogger, FileHandler, Formatter, StreamHandler, WARNING, DEBUG
# from sys import stdout, stderr
#
# stdout_logger = getLogger('stdout_logger')
# stdout_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
# fh_stdout = FileHandler('stdout.log')
# fh_stdout.setFormatter(stdout_formatter)
# stdout_handler = StreamHandler(stdout)
# stdout_handler.setFormatter(stdout_formatter)
# stdout_logger.addHandler(stdout_handler)
# stdout_logger.addHandler(fh_stdout)
# stdout_logger.setLevel(DEBUG)
#
# stderr_logger = getLogger('stderr_logger')
# stderr_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
# fh_stderr = FileHandler('stderr.log')
# fh_stderr.setFormatter(stderr_formatter)
# stderr_handler = StreamHandler(stderr)
# stderr_handler.setFormatter(stderr_formatter)
# stderr_logger.addHandler(stderr_handler)
# stderr_logger.addHandler(fh_stderr)
# stderr_logger.setLevel(WARNING)
#
#
# class Budget:
#     def __init__(self):
#         self.income = 0
#         self.expenses = 0
#         self.initial_income = 0
#         self.initial_expenses = 0
#
#     def add_income(self, amount):
#         if not isinstance(amount, (int, float)):
#             stderr_logger.error("Income amount must be a number.")
#             raise TypeError("Income amount must be a number.")
#         if amount < 0:
#             stderr_logger.exception('Klaida')
#             raise ValueError
#         stdout_logger.info('Baigta pridėti pajamų: ' + str(amount))
#         self.income += amount
#
#     def add_expense(self, amount):
#         if not isinstance(amount, (int, float)):
#             stderr_logger.error("Expense amount must be a number.")
#             raise TypeError("Expense amount must be a number.")
#         if amount < 0:
#             stderr_logger.error("Expense amount must be a positive number.")
#             raise ValueError("Expense amount must be a positive number.")
#         stdout_logger.debug('Baigta pridėti išlaidų: ' + str(amount))
#         self.expenses += amount
#
#     def get_balance(self):
#         return self.income - self.expenses
#
#     def reset_budget(self):
#         self.income = self.initial_income
#         self.expenses = self.initial_expenses
#
#
# # Example usage:
# my_budget = Budget()
# my_budget.add_income(2000)
# my_budget.add_expense('1000')
# my_budget.add_income(500)
# my_budget.add_expense(300)
# print("Current Balance:", my_budget.get_balance())  # Output: 1200
#
# my_budget.reset_budget()
# print("Balance after reset:", my_budget.get_balance())


from logging import getLogger, FileHandler, Formatter, StreamHandler, WARNING, DEBUG, ERROR
from sys import stdout, stderr

stdout_logger = getLogger('stdout_logger')
stdout_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh_stdout = FileHandler('stdout.log')
fh_stdout.setFormatter(stdout_formatter)
stdout_handler = StreamHandler(stdout)
stdout_handler.setFormatter(stdout_formatter)
stdout_logger.addHandler(stdout_handler)
stdout_logger.addHandler(fh_stdout)
stdout_logger.setLevel(DEBUG)

stderr_logger = getLogger('stderr_logger')
stderr_formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh_stderr = FileHandler('stderr.log')
fh_stderr.setFormatter(stderr_formatter)
stderr_handler = StreamHandler(stderr)
stderr_handler.setFormatter(stderr_formatter)
stderr_logger.addHandler(stderr_handler)
stderr_logger.addHandler(fh_stderr)
stderr_logger.setLevel(WARNING)


class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.initial_income = 0
        self.initial_expenses = 0

    def add_income(self, amount):
        if not isinstance(amount, (int, float)):
            error_message = "Income amount must be a number."
            stderr_logger.warning(error_message)
            raise TypeError(error_message)

        if amount < 0:
            error_message = "Income amount must be a positive number."
            stderr_logger.error(error_message)
            raise ValueError(error_message)

        success_message = f"Income of {amount} added successfully."
        stdout_logger.info(success_message)
        self.income += amount

    def add_expense(self, amount):
        if not isinstance(amount, (int, float)):
            error_message = "Expense amount must be a number."
            stderr_logger.warning(error_message)
            raise TypeError(error_message)

        if amount < 0:
            error_message = "Expense amount must be a positive number."
            stderr_logger.error(error_message)
            raise ValueError(error_message)

        success_message = f"Expense of {amount} added successfully."
        stdout_logger.debug(success_message)
        self.expenses += amount

    def get_balance(self):
        return self.income - self.expenses

    def reset_budget(self):
        self.income = self.initial_income
        self.expenses = self.initial_expenses


# Example usage:
my_budget = Budget()
my_budget.add_income('2000')
my_budget.add_expense(1000)
my_budget.add_income(500)
my_budget.add_expense(300)
print("Current Balance:", my_budget.get_balance())  # Output: 1200

try:
    my_budget.add_income("Not a number")
except TypeError as e:
    print(f"Error: {str(e)}")

my_budget.reset_budget()
print("Balance after reset:", my_budget.get_balance())
