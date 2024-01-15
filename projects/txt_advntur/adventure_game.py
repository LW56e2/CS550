"""
Name: Leo Wei
Date:
START - December 12th
RESTART - Jan 6th, 2023
END - Jan 14th, 2023

Sources:
https://www.pygame.org/docs/ref/music.html Pygame official documentation for playing audio
https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6 Royalty-free background music
https://www.youtube.com/watch?v=m9zhgDsd4P4 Mario Death sfx, here used as the death sfx

Reflection:
This project was an interesting one, and I learned many lessons apart from the programming. In the beginning,
I was planning out a relatively sophisticated structure for the adventure. The idea was to code the class
'StoryNode' and some subclasses (check out the code in /Abandoned\ project) and have a 'map' of all the
nodes, with each node doing something then pointing to another node. The storyline was also designed to
be very long. In fact, I spent about 7 hours on the airplane just writing out the storyline in a word
document. However, I realized that though my storyline might be cool, this was simply a text-based
adventure game. I figured the user would get bored if they played a text-based game for like more than
a couple of minutes. So I scrapped that plan, plus I was also getting really bored playing that game.

Then, I began to write another story still using the nodes system, this one based on Minecraft. I found
that also really hard to write and I was having a lot of issues. So I ended up just restarting completely,
which is what this game is. It is quite simple and the structure is easy-to-understand. I also made the
storyline much simpler and more comedic (I hope!). I also learned to use some basic tools to play audio
and added it to the game. In summary, while I restarted many times, I have learned that it might not
always be the best to write code in a complex structure over just a simple structure.


On my honor, I have neither given nor received unauthorized aid.
"""
import time  # For delays between prints
from pygame import mixer  # For playing audio


def play_background_music():
    """
    Play the 8-bit background music for practically forever.
    """
    mixer.init()  # Initialize pygame mixer
    mixer.music.load("audio/background_music.mp3")  # Load the background music through a relative path
    mixer.music.play(9999999)  # Play it on loop practically infinitely


def get_sleep_time(line: str):
    """
    Get the time that program should sleep between line prints.

    :param str line: The line that is being printed before the sleep.
    :return: The time that should be slept.
    :rtype: int
    """
    # To give the player time to read the message
    base_sleep_time = 0.3  # Base time of 0.3 seconds to prevent it from going too fast
    words_per_minute = 600
    words_per_second = words_per_minute / 60
    characters_per_second = words_per_second * 5  # 5 is the average word length
    dynamic_sleep_time = len(line) / characters_per_second
    total_sleep_time = base_sleep_time + dynamic_sleep_time  # Add the base and dynamic sleep times for total sleep time
    return total_sleep_time


def y_or_n():
    """
    Ask the user for a choice between yes (y) and no (n).

    :return: Boolean representing the player's choice (yes = True, no = False)
    :rtype: bool
    """
    invalid_response_message = 'Invalid response! Please type \"y\" or \"n\"'
    while True:
        user_input = input('>>> ').strip().strip('.').lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print(invalid_response_message)


def make_choice(prompt: str, choice_list: list):
    """
    Ask the user to choose between several options.

    :param str prompt: The text that is displayed to the user as a prompt.
    :param list choice_list: A lists of choices that the player can choose from.
    :return: The character that has been assigned to the chosen choice (e.g. "a" or "b")
    :rtype: str
    """

    invalid_response_message = 'Invalid Answer! Please enter the letter in front of the choice (e.g \"a\")\n'
    # To be displayed when the user enters an unrecognized response

    print('\n', end='')  # Add an extra line before the prompt
    for line in prompt.split('\n'):
        # The reason we don't print it directly is that we want time.sleep() between line prints
        print(line)
        time.sleep(get_sleep_time(line))  # To create the effect of time flowing
    print('\n', end='')  # Add an extra line before the choices
    character_choice_list = []  # Format: [['a',choice],['b',choice],...]

    for i, choice in enumerate(choice_list):  # enumerate() starts at 0 and numbers the elements by increments of 1
        character_in_prompt = chr(i + 97)  # chr(97) = 'a', chr(98) = 'b', etc
        choices_prompt = character_in_prompt + '. ' + choice
        print(choices_prompt)
        time.sleep(get_sleep_time(choices_prompt))
        character_choice_list.append([character_in_prompt, choice])  # Collect all the choices and characters into a single list
        # The character (like 'a', 'b', 'c', etc) are needed for checking for the player's responses

    print('\n', end='')  # Add an extra line before the input
    while True:
        # Wait until the player gives a valid response
        player_response = input('Select an option: ').strip().strip('.').lower()  # To prevent additional characters and capitalization
        for character_choice in character_choice_list:  # Iterate through the choices
            if player_response == character_choice[0]:  # Check if player input matches the character
                print('->', character_choice[1], '<-')  # Repeat the player's answers to them (not the letter/character, the answer)
                time.sleep(1)
                print('\n', end='')  # Add an extra line at the end
                return player_response  # Finally, return the player's choice

        print(invalid_response_message)


def game_over():
    """
    Tells the player that the game ended and asks if they would like to restart.

    :return: A boolean representing if the player would like to restart.
    :rtype: bool
    """
    mixer.init()
    mixer.music.load("audio/mario_death_sfx.mp3")  # Load the mario death sfx using a relative path
    mixer.music.play()  # This will override the background music that was playing
    print('You died! Game over!')
    print('Restart? (y/n)')
    return y_or_n()


def game_win(escape_route):
    """
    Tells the player they won the game and asks if they would like to try again.

    :param str escape_route: The escape route the player has achieved in this run.
    :return: A boolean representing if the player would like the play again.
    :rtype: bool
    """
    print('You won! Congratulations! You are now free!')
    print(f'You have achieved escape route {escape_route}')
    print('Would you like to try again, perhaps to find another escape route? (y/n)')
    return y_or_n()


def tp(text):
    """
    A timed print that adds a delay to the end of the print function

    :param str text: The text to print.
    """
    print(text)
    time.sleep(get_sleep_time(text))


def game_start_message():
    """
    A function that prints some messages before the game starts.
    """
    print('\n\n\n\n\n')  # To try to separate the game from the pygame init message
    # Use function tp() instead of print() for timing the messages
    tp('This game is meant for comedy and fun! Please do not take any of this seriously.')
    tp('Play with audio for a better experience!')
    print('\n\n')  # Space between instructions and actual game


def main_game():
    """
    The main prison escape text-based game.

    :return: A boolean representing if the player would like to continue playing.
    :rtype: bool
    """
    # This is where the main game starts
    # When the player dies, this is where they would restart from
    tp('You have been imprisoned! Oh no! You must find a way to escape.')

    # Using a while loop instead of game_over() which will be used in the future
    # Instead of killing the player when they choose the wrong option, we simply tell them it didn't work and ask them to try again
    while True:
        # Standard way of asking for the player to make a choice using function make_choice()
        choice = make_choice('What do you do?', ['Call for help', 'Try to break the iron bars', 'Use a drill to drill through the floor', 'Jump around in anger'])
        # Use the string selector for the options because that is what the function outputs (e.g. 'a' or 'b')
        if choice == 'a':
            # Use tp() over print() because tp() has a timed delay
            tp('What a terrible decision! No one responds and the guards come to shut you up.')
        elif choice == 'b':
            tp('It doesn\'t work. Who did you think you were, a superhero?')
        elif choice == 'c':
            tp('You don\'t know how to operate a drill and you drill into yourself.')
            return game_over()  # Return the value for checking if the player still wants to play
        elif choice == 'd':
            tp('You jump around and the floor breaks.')
            break
    tp('You fall down to a hallway.')
    tp('A guard sees you and is going to attack you!')
    choice = make_choice('What do you do?', ['Shoot the guard', 'Run to the the other way (Dead end)', 'Run to the right (Prison yard)', 'Run to the left (Stairs)'])
    if choice == 'a':
        tp('You shoot the prison guard and he dies.')
        tp('You feel bad for killing him and die of emotional damage.')
        # Punish the player with a death (which means a restart)
        # Remember to return the value and not simply call it
        # Returning it will allow for restarts
        return game_over()
    elif choice == 'b':
        tp('Oh no! You ran into a dead end!')
        choice = make_choice('You look around for options.', ['Climb the vent in the ceiling', 'Flip over a suspicious looking tile in the floor', 'Jump around in anger'])
        if choice == 'a':
            choice = make_choice('You can go either left or right. Both look about the same.', ['Go to the right', 'Go to the left'])
            if choice == 'a':
                tp('You crawl to the right, until the pipe starts going up.')
                tp('You see a vent at the top, with rays of sunlight coming in.')
                choice = make_choice('How do you climb up?', ['With your bare hands', 'Use a rope and hook it to the vent'])
                if choice == 'a':
                    tp('Your pants fall off and you die of embarrassment.')
                    return game_over()
                elif choice == 'b':
                    tp('It works and you climb up the rope.')
                    tp('You are now on top of the prison building, and you can see freedom right in front of you.')
                    choice = make_choice('How do you escape?', ['Jump down to the nearby lake', 'Jump to the tree', 'Jump to the hard concrete path'])
                    if choice == 'a':
                        tp('You realize you can\'t swim and drown.')
                        return game_over()
                    elif choice == 'b':
                        tp('Oh no. You just jumped back into the prison yard.')
                        tp('You step on on a branch, making a loud sound.')
                        tp('You suffer from the loud noise and die.')
                        return game_over
                    elif choice == 'c':
                        tp('You jump down and it brought back feelings from when you were riding the roller coaster in your teenage years.')
                        tp('You suddenly feel a rush of youth through your body and become immune to fall damage.')
                        # Provide a string to game_win() which is the escape route that the player achieved
                        # Also return the value instead of calling it to allow for retries
                        return game_win('A')
            elif choice == 'b':
                tp('You keep crawling to the left and eventually you reach another vent below you.')
                choice = make_choice('Climb out of the vent?', ['Yes', 'No'])
                if choice == 'a':
                    tp('You find yourself face-to-face with the head prison guard.')
                    choice = make_choice('Your heart almost leaped out of your ribs. What do you do?', ['Tell a funny joke', 'Tell an unfunny joke', 'Attempt to bribe him'])
                    if choice == 'a':
                        tp('The head prison guard laughs and tells you that you should be a comedian.')
                        tp('He releases you from the prison.')
                        return game_win('B')
                    elif choice == 'b':
                        tp('Maybe if you gave me some money I\'d let you go!')
                        tp('He shoots you with a gun.')
                        return game_over()
                    elif choice == 'c':
                        tp('You really thought giving me some money was gonna work?!')
                        tp('He shoots you with a gun.')
                        return game_over()
                elif choice == 'b':
                    tp('You keep crawling and smell a foul smell.')
                    tp('You inhale poisonous gas.')
                    return game_over()
        elif choice == 'b':
            tp('You find a secret underground passage!')
            tp('After entering, you find yourself in the middle of a pipeline.')
            choice = make_choice('Which direction do you run in?', ['Forward', 'Backwards'])
            if choice == 'a':
                tp('You run forwards and see a huge room of many pipelines.')
                choice = make_choice('Where should you go now?', ['Leap of faith', 'Activate your spider man superpowers', 'Call for help'])
                if choice == 'a':
                    tp('You don\'t have any faith so you fail the jump and instead trip over, landing head-first.')
                    return game_over()
                if choice == 'b':
                    tp('Nothing happened. Did you seriously think you were spider man?')
                    tp('The guard catches up to you and pushes you off the pipe.')
                    return game_over()
                if choice == 'c':
                    tp('You hear a response!')
                    tp('It was the spider friend that you made by saving his life!')
                    tp('He calls for his fellow spiders and they weave a spider silk web to trap the guard.')
                    tp('You see a manhole cover with a ray of light shining in above you.')
                    choice = make_choice('How do you get there?', ['Ask your spider friends for help', 'Try to parkour using the pipelines', 'Sit down'])
                    if choice == 'a':
                        tp('They crawl next to you to start making a ladder.')
                        tp('Your arachnophobia starts acting up and you suddenly feel a heaviness in your chest.')
                        return game_over()
                    if choice == 'b':
                        tp('You jump across the first 3 pipelines successfully.')
                        tp('On the fourth one, you slip and fall off.')
                        return game_over()
                    if choice == 'c':
                        tp('You sit down and look down, taking a short break.')
                        tp('You realize that you are sitting on a carpet - a magic carpet!')
                        tp('You start floating and successfully escaped by floating to open the manhole cover.')
                        return game_win('C')
            elif choice == 'b':
                tp('Running backwards was a really bad idea.')
                tp('Because you cannot see where you are running, you trip and fall.')
                return game_over()
        elif choice == 'c':
            tp('What did you think jumping around was going to do?!')
            tp('The prison guard shoots you.')
            return game_over()
    elif choice == 'c':
        tp('You run to a outdoors prison yard.')
        tp('You step on a branch, making a loud sound.')
        tp('Your suffer from the loud noise and die.')
        return game_over()
    elif choice == 'd':
        tp('You run to the stairs!')
        choice = make_choice('Which way should you go?', ['Go up the stairs', 'Go down the stairs'])
        if choice == 'a':
            tp('You walk 5 steps.')
            tp('You got too tired and the guard catches you.')
            return game_over()
        elif choice == 'b':
            tp('You look down the long flight of stairs and feel scared.')
            tp('You remember when your brother fell down the stairs and you passed out and rolled down the stairs.')
            return game_over()


# Program execution
if __name__ == '__main__':
    play_background_music()  # Start playing music when game starts
    game_start_message()  # The message before the game actually starts.
    # Separated from main_game() because we don't want the player to read this again after they restart
    while True:
        if not main_game():  # Checks for when the player no longer wants to play
            break
        else:
            play_background_music()  # Restart the music because it was stopped when death sfx played


'''
Peer reviews:

Lexie (classmate): "I think your game is great! I like the touches you gave it. I really think everything about your game is perfect, you should just close the
file and click submit. The text is legible and good."

Response: I noticed that his reading speed was a bit behind the text and having some difficulty reading, so I decreased the speed and added newlines. He also 
failed many times and felt maybe a bit annoyed, so I added more valid escape routes and less deaths.

Max (classmate): "I think you should probably edit that [inappropriate] part out, and change it to like the guard caught you or something. Also there is that
empty space, change that, umm the reading speed is pretty good, maybe slightly faster, I like how the options are presented."

Response: I increased the reading speed slightly, and edited the inappropriate part out, and deleted the accidental empty option.
'''
