from entry import Entry

class ExpensesEntry(Entry):
    def __init__(self, amount, payment_option, received_good_or_service):
        super().__init__(amount)
        self.payment_option = payment_option
        self.received_good_or_service = received_good_or_service

    def __str__(self):
        return f'Expenses: {self.amount}, Payment option: {self.payment_option}, Received good or service: {self.received_good_or_service}'
