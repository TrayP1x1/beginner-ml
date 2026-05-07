import random

# Hangman visuals stored as strings to be printed line-by-line as the player loses
rope = "|      |       |"
head = "|      O       |"
chest = "|    --|--     |"
belly = "|      |       |"
legs = "|    _/ \\_     |"

# List of possible words and the visual parts ordered by "missed chance"
words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
hangman = [rope, head, chest, belly, legs]

# Initialize game state: pick a word and create the hidden version (underscores)
random_word = random.choice(words)
random_word_in_list = list(random_word)
incomplete_word = []  # Temp list to build the display word each turn
list_of_underscores = ["_" for letter in random_word_in_list]
chosen_letters = []  # Tracks all letters the user has guessed

chances = 0
correct = False

print(f"The word is {list_of_underscores}")
print("\n")

# Main game loop: continues until 5 mistakes are made or the word is found
while (chances != 5) and (not correct):
    # Use .strip() to clean up accidental whitespace in the input
    guess = input("Choose a letter: ").strip()

    # Store the guess so we know which letters to reveal
    if guess not in chosen_letters:
        chosen_letters.append(guess)

    # Logic for a CORRECT guess
    if guess in random_word_in_list:
        # Rebuild the display word by checking every letter in the target word
        for index in range(len(random_word_in_list)):
            if random_word_in_list[index] in chosen_letters:
                incomplete_word.append(random_word_in_list[index])
            else:
                incomplete_word.append("_")

        # Print the current hangman status even on correct guesses
        for i in range(chances):
            print(hangman[i])

    # Logic for an INCORRECT guess
    else:
        chances += 1
        print(f"No {guess} in word, you have {5-chances} guesses left")
        print("----------------")
        for i in range(chances):
            print(hangman[i])
        print("----------------")
        print("\n")

    # Show the current progress (e.g., ['p', '_', 't', 'h', 'o', 'n'])
    if len(incomplete_word) > 0:
        print(incomplete_word)

    # Check Win Condition: if the built word matches the target word
    if incomplete_word == random_word_in_list:
        correct = True

    # Reset the temp word builder for the next turn
    incomplete_word = []

# Final game result
if chances == 5:
    print(f"You lost! The word was: {random_word}")
if correct:
    print("You won!")
