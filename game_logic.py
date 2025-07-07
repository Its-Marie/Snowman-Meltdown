import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters =[]
    mistakes = 0
    max_mistakes = len(STAGES) -1
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Game-Loop
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess! The snowman is melting...\n")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You won! The snowman is safe.")
            return

    # if lose
    display_game_state(mistakes, secret_word, guessed_letters)
    print("The snowman melted! The word was:", secret_word)

if __name__ == "__main__":
    play_game()
