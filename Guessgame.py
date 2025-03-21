import random  #this is a like a toolbox which is used when we have to write a random number 
secret_number = random.randint(1,10); #inside the random library we have the funstion which is used to select between two numbers
guess = None
while guess!= secret_number:
    guess=int(input('guess a number between 1 and 10 :'))

    if guess>secret_number:
        print('the number is too high')
    elif guess < secret_number:
        print('number is too low')

    else :
        print("you have won")

