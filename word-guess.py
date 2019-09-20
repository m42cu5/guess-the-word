import random

words = ["apple", "banana", "orange"]
word = random.choice(words)
clue = list("_" * len(word))
guess = ""
nbr_of_guesses = 0

while guess != word:
    guess = input(f'Guess the word "{"".join(clue)}": ').lower()
    nbr_of_guesses += 1
    if guess != word:
        if len(guess) == 1:
            occurrences = word.count(guess)
            position = 0
            while occurrences > 0:
                occurrences -= 1
                position = int(word.find(guess, position, -1))
                clue[position] = guess
                position += 1
            guess = "".join(clue)
print(f'''Correct! The word was "{word}".
You guessed the word in {nbr_of_guesses} guess(es)''')
