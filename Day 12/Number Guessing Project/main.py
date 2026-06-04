import art
import random

HARD = 5
EASY = 10

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

num = random.randint(1,100)
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else:
        return HARD

def game():
    print(art.logo)
    print("Welcome to Number Guessing Game: ")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    while turns:
        print(f"You have {turns} left over")
        guess = int(input("Enter a number from 1 - 100: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()



# num = random.randint(1,100)
# level = input("want to play 'easy' level or 'hard' : ").lower()
# if level == "easy":
#     attempts = 10
# else:
#     attempts = 5
# while attempts:
#     guess = int(input("Chosse a number from 1 to 100: "))
#     if guess == num:
#         print("actual answer is: ", num)
#         break
#     elif guess < num:
#         print("too low")
#     elif guess > num:
#         print("too high")
#     attempts -= 1
#     print(f"You have {attempts} remaining attempts: ")


