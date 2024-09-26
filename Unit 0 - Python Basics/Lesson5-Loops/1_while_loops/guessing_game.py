import random
secret_number = random.randint(1,10)
print(f'Secret:{secret_number}')
guess = None
while guess != secret_number:
    guess = int(input("Guess the number(1-10):"))
    if guess < secret_number:
        print('too low!')
    elif guess > secret_number:
        print('too high!')
print(f'Congrats! You guessed the number {guess}')