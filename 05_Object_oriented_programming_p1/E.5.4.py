# -----------------------------------------------
# P.5.4
# -----------------------------------------------
# • Perdaryti 1 užduotį taip, kad spausdinant sakinio objektą, spausdintų ne
#   objekto adresą, o įvestą tekstą.
# • Perdaryti 2 užduotį taip, kad spausdinant datos objektą, spausdintų ne
#   objekto adresą, o įvestą datą.
# -----------------------
# • Refactor the first program (exercise no. 1) so that when printing the
#   object, instead of its address the text attribute's value would be printed.
# • Refactor the second program (exercise no. 2) so that when printing the
#   object, instead of its address the date attribute's value would be printed.
# -----------------------------------------------
import datetime

class Text:

    def __init__(self, text):
        self.text = text

    def return_text_backwards(self):
        return self.text[::-1]

    def return_text_lowercase(self):
        return self.text.lower()

    def return_text_uppercase(self):
        return self.text.upper()

    def return_index(self, index):
        words = self.text.split()
        return words[index]

    def count_text_and_characters(self):
        words = self.text.split()
        word_count = len(words)
        character_count = len(self.text)
        return word_count, character_count

    def text_replace(self, old, new):
        return self.text.replace(old, new)

    def how_many_words(self):
        word_count = f'Words count: {len(self.text.split())}'
        cap_count = f'Cap letters: {sum(True for letter in self.text if letter.isupper())}'
        lower_count = f'Low letters: {sum(True for letter in self.text if letter.islower())}'
        numbers_count = f'Numbers: {sum(True for letter in self.text if letter.isdigit())}'
        return word_count, cap_count, lower_count, numbers_count

    def __str__(self):
        return self.text


text1 = Text('Zen of Python 123')
text2 = Text('Life is life')
print(text1)
print(text2)

# -----------------------------------------------


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
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True

        return False

    def minus_days(self, days: int) -> datetime.date:
        return self.date - datetime.timedelta(days=days)

    def add_days(self, days: int) -> datetime.date:
        return self.date + datetime.timedelta(days=days)

    def __str__(self):
        return str(self.date)


anni_1 = Anniversary(datetime.date(2020, 6, 8))
print(anni_1)


# print("Years: ", anni_1.years_passed())
# print("Weeks: ", anni_1.weeks_passed())
# print("Days: ", anni_1.days_passed())
# print("Hours: ", anni_1.hours_passed())
# print("Minutes: ", anni_1.minutes_passed())
# print("Seconds: ", anni_1.seconds_passed())
# print("Is anniversary in leap year?", anni_1.leap_year())
# print("Subtract days: ", anni_1.minus_days(10))
# print("Add days: ", anni_1.add_days(10))