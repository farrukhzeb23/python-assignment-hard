import random
import os


class Hangman:
    """
        This is test docs
    """

    # This can be fetched from DB
    words = [
        "cat",
        "elephant",
        "umbrella",
        "ghost",
        "rhythm",
        "kangaroo",
        "island",
        "submarine",
        "wizard",
        "oxygen"
    ]

    def __init__(self):
        self.word_to_guess = random.choice(self.words).lower()
        # print(self.word_to_guess)
        self.guessed_letters = []
        self.max_wrong_guesses = 6
        self.wrong_guesses = 0

    def greeting_message(self):
        print("Welcome to Hangman!\n")

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display

    def is_game_over(self):
        return self.wrong_guesses >= self.max_wrong_guesses or self.is_word_guessed()

    def get_guess(self):
        while True:
            guess = input("\nGuess a letter: ").lower()
            if len(guess) > 1 or guess.isdigit():
                print("Please enter a single letter")
            else:
                return guess

    def make_guess(self, letter):
        self.guessed_letters.append(letter)
        if letter not in self.word_to_guess:
            self.wrong_guesses += 1
            print("\nIncorrect!\n")

    def is_word_guessed(self):
        return all(letter in self.guessed_letters for letter in self.word_to_guess)

    def clear_screen(self):
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For Linux / macOS
        else:
            os.system('clear')

    def display_hangman(self):
        stages = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
        ]
        print(stages[self.wrong_guesses])

    def play_game(self):
        while not self.is_game_over():
            self.greeting_message()
            self.display_hangman()
            print(self.display_word())
            guess = self.get_guess()
            self.make_guess(guess)
            self.clear_screen()

        if self.is_word_guessed():
            print("\nYou've won 🥳\n")
        else:
            print(f"\nYou've lost 🥲\nWord was {self.word_to_guess}\n")


if __name__ == "__main__":
    hangman = Hangman()
    hangman.play_game()
