# -----------------------
# • Write a program which would print a desired word every X seconds. The
#   program should:
#   • Ask a user to enter the number of seconds (X).
#   • Ask a user to enter a word, and print it every X seconds.
#   • If the format of the seconds (X) is incorrect, ask the user to enter the
#     number of seconds again.
# -----------------------------------------------

import time

word = input("Enter word: ")

while True:
    try:
        seconds = int(input("Enter waiting interval in seconds:"))
        while True:
            time.sleep(seconds)
            print(word)
    except ValueError:
        print("Enter a valid positive integer")
