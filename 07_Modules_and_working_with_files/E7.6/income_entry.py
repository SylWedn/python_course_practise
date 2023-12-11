from entry import Entry

class IncomeEntry(Entry):
    def __init__(self, amount, sender, additional_info):
        super().__init__(amount)
        self.sender = sender
        self.additional_info = additional_info

    def __str__(self):
        return f'Income: {self.amount}, Sender: {self.sender}, Additional info: {self.additional_info}'
