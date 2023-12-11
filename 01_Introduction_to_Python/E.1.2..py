text = "Zen of Python"
last_letter = text[12]
print ("last letter:",last_letter)

first_letter = text[7:][0]
print ("first letter:",first_letter)

first_word = text[0:2]
print ("first word:", first_word)

last_word = text[9:12]
print ("last word:",last_word)

reverse_text = text[::-1]
print("reverse text:",reverse_text)

word = text.split()
first_word = word[0]
second_word = word[1]
third_word = word[2]

print (first_word)
print (second_word)
print (third_word)

new_text = text.replace("Python", "Programming")
print (new_text)