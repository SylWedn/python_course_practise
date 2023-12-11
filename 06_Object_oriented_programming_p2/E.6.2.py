from datetime import datetime, timedelta


class Employee:

    def __init__(self, name, hourly_wage, employed_since):
        self.name = name
        self.hourly_wage = hourly_wage
        self.employed_since = datetime.strptime(employed_since, '%Y-%m-%d')

    def __str__(self):
        return f'Employee {self.name} works since {self.employed_since} and their hourly wage is {self.hourly_wage} $.'

    def count_days_employed(self):
        days_worked = datetime.now() - self.employed_since
        days = divmod(days_worked.days, 1)
        return days[0]

    def calc_total_wage(self):
        return f'Employee {self.name} has been paid {self.hourly_wage * self.count_days_employed() * 8} $'


class NormalEmployee(Employee):

    def count_days_employed(self):
        days = (datetime.now() - self.employed_since).days + 1

        work_days = 0
        for day in range(days):
            date = self.employed_since + timedelta(days=day)
            if date.weekday() < 5:
                work_days += 1
        return work_days

    def calc_total_wage(self):
        return f'Employee {self.name} has been paid {self.hourly_wage * self.count_days_employed() * 8} $'


employee1 = Employee('Antanas', 12, '2021-05-15')
employee2 = NormalEmployee('Jonas', 13, '2017-08-12')

print(employee1)
print(employee1.calc_total_wage())
print('-' * 20)
print(employee2)
print(employee2.calc_total_wage())
