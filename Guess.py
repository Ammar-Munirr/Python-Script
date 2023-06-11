import random
print('############ Welcom to my guessing game ############')
print('I am thinking of a number between 1 to 100')
print('Try to guess it with few attempts')
secret_number=random.randint(1,100)
attempts=0
while True:
    try:
     user_guess=int(input('Enter Your Guess: '))
     attempts += 1
     if user_guess>secret_number:
         print('Upper....')
         continue
     if user_guess<secret_number:
         print('Lower....')
         continue
     if user_guess == secret_number:
         print('Congrats')
         print('You have Guessed the number in total',attempts,'attempts')
         break
    except ValueError:
        print('Please Enter Only Integer Number')
