import random

class Hangman:
    def __init__(self):
        self.words = ["PROGRAMMING", "PYTHONIC", "DEVELOPER", "HANGMAN", "ALGORITHMS"]
        self.stages = [
            " +---+\n |   |\n     |\n     |\n     |\n     |\n=========",
            " +---+\n |   |\n O   |\n     |\n     |\n     |\n=========",
            " +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========",
            " +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========",
            " +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n=========",
            " +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n=========",
            " +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n========="
        ]
        self.max_tries = len(self.stages) - 1

    def print_tile(self):
        print(self.stages[self.incorrect_guesses])

    def display_word(self):
        display = [letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess]
        return ' '.join(display)

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").upper()
            if guess.isalpha() and len(guess) == 1:
                return guess
            else:
                print("\nInvalid input. Please enter a single letter.")

    def update_game_state(self, guess):
        if guess in self.guessed_letters:
            print("You already guessed that letter.")
        elif guess in self.word_to_guess:
            self.guessed_letters.add(guess)
            print("\nGood guess!")
        else:
            self.guessed_letters.add(guess)
            self.incorrect_guesses += 1
            print("\nIncorrect guess.")

    def play_game(self):
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        
        print("Welcome to Hangman!")
        print(self.display_word())

        while self.incorrect_guesses < self.max_tries:
            self.print_tile()
            print(f"Word: {self.display_word()}")
            print(f"Guesses remaining: {self.max_tries - self.incorrect_guesses}")
            
            guess = self.get_guess()
            self.update_game_state(guess)

            if set(self.word_to_guess) <= self.guessed_letters:
                print(f"Congratulations! You've guessed the word: {self.word_to_guess}")
                return

        self.print_tile()
        print(f"Game over! The word was: {self.word_to_guess}")
