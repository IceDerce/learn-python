number = 23
guess = int(input(
        'Enter an integer :'
))


if guess == number:
    print('Congratulations!You make it!\n'
          'But you are not awarded anything!')
elif guess < number:
    print('No,your guess is too low')
else:
    print('No,your number is too high')