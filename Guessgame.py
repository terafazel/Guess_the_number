import random # the library is called so that we can use the random function inside this library
secret_numbers=random.randint(1,10);#the  number that the local machine is going to select is then stored in a vairblae 
guess_number=None #a variable is defined which is going to store the value of the customer , whjich is none so that there is no garbage value 
attempts=0# attempts are set as 0 as they are going to fundamentally be used fot increment after everylooop when there is a wrong attmempt to guess the number 
max_attempts=int(input('enter the number of attempts you can make to get the right answer'))#this is used to get the threshold attempt that the used thinks can he make thje right answer, the value is stored inside the maz attmepts vairbale 
while guess_number!=secret_numbers and attempts < max_attempts:#so here we are using two concepts one is the confitional loops and the other is the conditional logic the conditional loop is ussed to make sure that the bumber guess by the user is not same then there is the and logic to make sure that both the condition is satisfied  
    guess_number= int(input('enter a number between 1 and 10:'))#take the input from the user 
    attempts=attempts+1 # increment the number every time someone makes the attempt 
    attempts_left=max_attempts-attempts# check the number of attempts are left
   

    if guess_number>secret_numbers:
        print('number is greater than the secret number')
        print(f'the number of attempts left for the user is  {attempts_left}')
    elif guess_number<secret_numbers:
        print('number is less than the secret number')
        print(f'the number of attempts left for the user is  {attempts_left}')

    else:
        print('hurray you have the same number')
    
if guess_number!=secret_numbers:
    print('sorry you attempts have exhausted better luck next time')

