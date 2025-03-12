import random

lowest_number = 1
highest_number = 100
guesses = 0
is_running = True
answer = random.randint(lowest_number, highest_number)

while is_running:
     guess = input(f"Enter a number from {lowest_number} and {highest_number}: ")
     guess = int(guess)
     if guess > highest_number or guess < lowest_number:
         print(f"Please Enter a number from {lowest_number} and {highest_number}: ")
     elif guess < answer:
         print("Your answer is lower than the answer. Try again")
         guesses += 1
     elif guess > answer:
         print("Your answer is higher than the answer. Try again")
         guesses += 1
     elif guess == answer:
         print(f"Your answer {answer} is correct!")
         print(f"Number of guesses: {guesses}")
         is_running = False