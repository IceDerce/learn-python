number = 56
runing = True

while runing:
    guess = int(input('Input a integer:'))

    if guess == number:
        print('Yes,you are right!')
        runing = False
    elif guess < number:
        print('No,your guess is too low')
    else:
        print('No,your guess is too high')
else:
    print('\nThe game is over!')