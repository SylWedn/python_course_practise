import datetime


# -----------------------------------------------
# P.5.3
# -----------------------------------------------
# • Perdaryti 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas,
#   veiksmai turi būti atliekami su „Zen of Python“ tekstu.
# • Perdaryti 2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data,
#   veiksmai turi būti atliekami su programuotojo gimtadieniu.
# -----------------------
# • Refactor the first program (exercise no. 1) so that if no text is given
#   when creating an object, the default text would be "Zen of Python".
# • Refactor the second program (exercise no. 2) so that if no date is given
#   when creating an object, the default date would be your birthday.
# -----------------------------------------------


class Text:

    def __init__(self, text='Zen of Python'):
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


text1 = Text()

print(text1.return_text_backwards())
print(text1.return_text_lowercase())
print(text1.return_text_uppercase())
print(text1.return_index(1))
print(text1.count_text_and_characters())
print(text1.text_replace('Zen', 'hello'))
print(text1.how_many_words())

print(40 * '_')

current_date = datetime.datetime.now()


class Anniversary:

    def __init__(self, date=datetime.datetime(1992, 12, 4)):
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


anni_1 = Anniversary()  # No need to pass datetime.datetime(None)

print("Years: ", anni_1.years_passed())
print("Weeks: ", anni_1.weeks_passed())
print("Days: ", anni_1.days_passed())
print("Hours: ", anni_1.hours_passed())
print("Minutes: ", anni_1.minutes_passed())
print("Seconds: ", anni_1.seconds_passed())
print("Is anniversary in leap year?", anni_1.leap_year())
print("Subtract days: ", anni_1.minus_days(10))
print("Add days: ", anni_1.add_days(10))

