# Guess_the_number
the game is designed using the random function and the while , if else if loop 


1. Import the Library
python
Copy
Edit
import random
🧠 Explanation:
We import the random library, which is a built-in Python library. It contains many functions that help us work with random numbers.

2. Generate a Secret Number
python
Copy
Edit
secret_number = random.randint(1, 10)
🧠 Explanation:
We use random.randint(1, 10) to generate a random number between 1 and 10, including both 1 and 10.
This number is stored in a variable called secret_number, which the player has to guess.

✅ random → the library
✅ randint() → a built-in function inside the random library
✅ secret_number → holds the randomly chosen number
3. Create a Placeholder for the User's Guess
python
Copy
Edit
guess = None
🧠 Explanation:
Before the user starts guessing, we set guess to None (which means “nothing” or “empty” in Python).
We do this so we can compare guess to secret_number in the loop.

4. Start the Loop: Let the User Guess
python
Copy
Edit
while guess != secret_number:
🧠 Explanation:
We use a while loop to keep the game going until the user guesses the correct number.

This means:

“As long as the guess is not equal to the secret number, keep asking the user to guess again.”

5. Take Input and Give Hints Using if-else
python
Copy
Edit
guess = int(input("Guess a number between 1 and 10: "))

if guess > secret_number:
    print("Too high!")
elif guess < secret_number:
    print("Too low!")
else:
    print("You got it!")
🧠 Explanation:

First, we ask the user to input a number.
We convert the input from string to integer using int().
Then we use if, elif, and else to compare:
If guess is too high, we give a hint.
If guess is too low, we give a different hint.
If guess is correct, we congratulate the user.
✨ Final Version of Your Explanation (Clean and Clear):
We start by importing the random library, which gives us access to built-in functions to generate random numbers.
Then we create a secret number using random.randint(1, 10) and store it in a variable.
We create a variable called guess and set it to None to start with.
Using a while loop, we keep running the game until the user guesses the correct number.
Inside the loop, the user is asked to enter a number, and we give hints using if, elif, and else depending on whether the guess is too high, too low, or correct.
