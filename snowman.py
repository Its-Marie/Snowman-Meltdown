from game_logic import play_game

def main():
    print("Welcome to Snowman Meltdown!")

    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Snowman Meltdown!")
            break

if __name__ == "__main__":
    main()
