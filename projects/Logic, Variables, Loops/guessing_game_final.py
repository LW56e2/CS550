import random

range = (1,100)
points = 0
guesses_counter = 0
max_tries = None
playing = True

while True:
    answer = random.randint(range[0],range[1])
    print('Okay, lets play a round of the guess-my-number game!')
    if max_tries == 0:
        print('Since you took 1 try to guess the previous number, I\'ll still give you 1 try for this number.')
        max_tries = 1
    elif max_tries == None:
        pass
    elif max_tries == 1:
        print(f'You have {max_tries} chance to guess the number!')
    else:
        print(f'You have {max_tries} chances to guess the number!')
    print(f'Guess my number between {range[0]} and {range[1]} (inclusive)')
    while True:
        while True:
            try:
                guess = int(input("Your guess: "))
                break
            except ValueError:
                print('Please input a number.')
        guesses_counter += 1
        if guess == answer:
            print('Correct! That was a great guess! You win!')
            print(f'You get one point!')
            points += 1
            print(f'You now have {points} points!')
            if guesses_counter != 1:
                print(f'It took you {guesses_counter} tries.')
                max_tries = guesses_counter - 1
                guesses_counter = 0
            else:
                print(f'It only took you {guesses_counter} try! Amazing!!!')
                max_tries = guesses_counter - 1
                guesses_counter = 0
            break
        elif guess > range[1]:
            print(f'I told you the answer was between {range[0]} and {range[1]}! What use is guessing this high?')
        elif guess < range[0]:
            print(f'I told you the answer was between {range[0]} and {range[1]}! What use is guessing this low?')
        elif guess > answer:
            print('That was too high. Try guessing lower!')
        elif guess < answer:
            print('That was too low. Try guessing higher!')

        if max_tries != None:
            if max_tries <= guesses_counter:
                print(f'You lose because you already used your {max_tries } tries!')
                print(f'You earned {points} points.')
                playing = False
                break

    if playing == False:
        break

    continue_playing = input('Do you wish to continue playing? (y/n)').lower().strip()
    if continue_playing == 'n':
        print(f"Whatever, you still earned {points} points though!")
        break
    elif continue_playing != 'y':
        print('I\'ll take that as a no then.')
        print(f"Whatever, you still earned {points} points though!")
        break



