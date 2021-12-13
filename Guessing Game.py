print ('Rules')
print('-----')
print('Guess a number from 1-20')
print('You get 3 tries')
print('Enjoy :)')

secret_number = 15
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == secret_number:
        print('You won! The correct number was 15')
        break
else:
    print('Sorry you failed')
















