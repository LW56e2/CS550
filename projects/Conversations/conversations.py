'''
Name: Leo Wei
Data: 2023 Nov 30
Reflection:


Sources: None

On my honor, I have neither given nor received unauthorized aid.
'''

import time
world_life_expectancy = 72.27

print("Hey.")
time.sleep(2)
age = int(input("How old are you?\n>>> "))


time_left = round(world_life_expectancy-float(age),2)
percent_lived_through = float(age)/world_life_expectancy*100

print(f"You are {time_left} years away from reaching your life expectancy.")
time.sleep(2)
print(f"So that means, on average, you have {time_left} more years to live.")
time.sleep(2)
print(f"And you are {age} years old.")
time.sleep(2)
print(f"You have lived through {round(percent_lived_through,2)}% of your life already.")
time.sleep(2)
print("Do something useful for your life.")
time.sleep(2)

progress_bar_length = 50
progress_bar_divisor = 100/progress_bar_length
progress_bar_completed = round(percent_lived_through/progress_bar_divisor)
progress_bar_incomplete = progress_bar_length-progress_bar_completed

progress_bar_string = '<'
for i in range(progress_bar_completed):
    progress_bar_string += '='
for i in range(progress_bar_incomplete):
    progress_bar_string += '.'
progress_bar_string += '>'

print(progress_bar_string)
time.sleep(2)
print("That\'s your life turned into a progress bar")

