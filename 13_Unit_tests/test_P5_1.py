# • Create a class named Sentence which would have one attribute named text,
#   the string value of which would be set at the time of creating an object of
#   this class. Also, write the methods for the class such that they would:
#
#   • Return the value of the sentence (of its text attribute) in reverse.
#   • Return the sentence in all lowercase letters.
#   • Return the sentence in all uppercase letters.
#   • Return a word from the sentence by its index (which is passed as an
#     argument to the method). Treat the words as the parts of the sentence
#     separated by spaces " ".
#   • Return how many words and how many characters the sentence contains.
#   • Return the sentencede with a changed word or a changed character in it,
#     depending on the arguments passed to the method: the first argument is a
#     character or word to be changed, and the second argument is a new character
#     or word to be written instead.
#   • Prints how many words, numbers, uppercase and lowercase letters there are
#     in the sentence.
#
# • Create several objects of this class and try out all the methods.
# -----------------------------------------------

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


text1 = Text('Zen of Python 123')

print(text1.return_text_backwards())
print(text1.return_text_lowercase())
print(text1.return_text_uppercase())
print(text1.return_index(0))
print(text1.count_text_and_characters())
print(text1.text_replace('Zen', 'hello'))
print(text1.how_many_words())
