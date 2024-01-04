'''

Name: Leo Wei
Data: 2023 Nov 30
Reflection:
I found this project very fun while I worked on it, and I tried to go beyond what was required. I became more experienced
in using APIs as well as writing code faster. I also improved my debugging skills and it is only my second time using the
module 'logging', and it helped in controlling the debug messages.

Sources:
https://platform.openai.com/docs/api-reference/introduction
https://docs.python.org/3/library/textwrap.html

On my honor, I have neither given nor received unauthorized aid.

'''

import random

range = (1,100)

answer = random.randint(range[0],range[1])
player_answer = None

print(f'Let\'s play a guessing game! Try to guess the number that I chose between {range[0]} and {range[1]}.')
while player_answer != answer:
    while True:
        try:
            player_answer = int(input("Your guess: "))
            break
        except ValueError:
            print('Please input a number.')
    if player_answer == answer:
        print('Correct! That was a great guess! You win!')
        break
    elif player_answer > range[1]:
        print(f'I told you the answer was between {range[0]} and {range[1]}! What use is guessing this high?')
    elif player_answer < range[0]:
        print(f'I told you the answer was between {range[0]} and {range[1]}! What use is guessing this low?')
    elif player_answer > answer:
        print('That was too high. Try guessing lower!')
    elif player_answer < answer:
        print('That was too low. Try guessing higher!')