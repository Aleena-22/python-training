# Implement the Guess-my-Number game in the OOP framework

#     Computer has chose a number (1, 100), can you guess? Max. 10 guesses

#     -> 35
#     Higher

#     -> 65
#     Lower

#     -> 44
#     Higher

#     -> 45
#     Correct!!

#     Number of attempts 4/10
#     Excellent playing!

import random

class GuessMyNumberGame():
    def __init__(self, name, max_attempts = 0):
        self.name = name
        self.max_attempts = max_attempts
        self.attempts = 0
        self.guess_number = random.randint(1, 100)

    def play(self):
        print(f"Computer has chosen a number between 1 and 100. So guess a number")

        while self.attempts < self.max_attempts:
            try:
                guess = int(input(" -> "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            self.attempts += 1

            if guess < self.guess_number:
                print("Higher")
            elif guess > self.guess_number:
                print("Lower")
            else:
                print("Correct!!")
                self.display_results()
                return
               
        print("Better luck next time")
        print(f"The correct number was {self.guess_number}")

    def display_results(self):
        print(f"\nNumber of attempts {self.attempts}/{self.max_attempts}")
        if self.attempts <= 4:
            print("Excellent")
        elif self.attempts <= 7:
            print("Good")
        else:
            print("You can do better!")

# Test
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = GuessMyNumberGame(player_name, max_attempts=10)
    game.play()

