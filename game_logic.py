import random
from ascii_art import STAGES

# list of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """chose random words from list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + "=" * 40)
    print(f"Mistakes: {mistakes} / {len(STAGES) - 1}")
    print(STAGES[mistakes])

    display_word = " ".join([
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ])
    print(f"Word:     {display_word}")
    print(f"Guessed:  {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print("=" * 40 + "\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical letter.\n")
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
