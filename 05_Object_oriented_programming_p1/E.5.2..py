import datetime

current_date = datetime.datetime.now()


class Anniversary:
    def __init__(self, date: datetime.date):
        self.date = date

    def years_passed(self):
        return round((current_date - self.date).days / 365, 2)

    def weeks_passed(self):
        return round((current_date - self.date).days / 7, 2)

    def days_passed(self):
        return round((current_date - self.date).days, 2)

    def hours_passed(self):
        return round((current_date - self.date).days * 24, 2)

    def minutes_passed(self):
        return round((current_date - self.date).days * 24 * 60)

    def seconds_passed(self):
        return round((current_date - self.date).days * 24 * 60 * 60)

    def leap_year(self):
        year = self.date.year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def minus_days(self, days: int) -> datetime.date:
        return self.date - datetime.timedelta(days=days)

    def add_days(self, days: int) -> datetime.date:
        return self.date + datetime.timedelta(days=days)


anni_1 = Anniversary(datetime.datetime(2013, 4, 8))

print("Years: ", anni_1.years_passed())
print("Weeks: ", anni_1.weeks_passed())
print("Days: ", anni_1.days_passed())
print("Hours: ", anni_1.hours_passed())
print("Minutes: ", anni_1.minutes_passed())
print("Seconds: ", anni_1.seconds_passed())
print("Is anniversary in leap year?", anni_1.leap_year())
print("Subtract days: ", anni_1.minus_days(10))
print("Add days: ", anni_1.add_days(10))
