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


# print(text1.return_text_backwards())
# print(text1.return_text_lowercase())
# print(text1.return_text_uppercase())
# print(text1.return_index(1))
# print(text1.count_text_and_characters())
# print(text1.text_replace('Zen', 'hello'))
# print(text1.how_many_words())