import logging
import time
import sys



logging.basicConfig(level=logging.DEBUG)


def get_sleep_time(line: str):
    """
    Get the time that program should sleep between line prints.

    :param str line: The line that is being printed before the sleep.
    :return: The time that should be slept.
    :rtype: int
    """
    # To give the player time to read the message
    base_sleep_time = 0.4  # Base time of 0.4 seconds to prevent it from going too fast
    words_per_minute = 800
    words_per_second = words_per_minute / 60
    characters_per_second = words_per_second * 5  # 5 is the average word length
    dynamic_sleep_time = len(line) / characters_per_second
    total_sleep_time = base_sleep_time + dynamic_sleep_time
    return total_sleep_time


class StoryNode:
    """
    One general point/event in the adventure game.

    Attributes:
    coordinates (tuple): The location of the node. Other nodes can point to this node.
    prompt (str): The prompt displayed to the user.
    """

    def __init__(self, coordinates: tuple[int, int], prompt: str) -> None:
        """
        Initialize the coordinates and prompt for node.

        :param tuple coordinates: The location of the node. Other nodes can point to this node.
        :param str prompt: The prompt displayed to the user.
        """
        self.coordinates = coordinates
        self.prompt = prompt


class ChoiceNode(StoryNode):
    """
    A type of node that is a choice the player must make.

    Attributes:
    coordinates (tuple): The location of the node. Other nodes can point to this node.
    prompt (str): The prompt displayed to the user.
    choice_list (list): A list of multiple choices and conditions as well as consequences of these choices.
    player: The player, for alternative choices and effects.
    """

    def __init__(self, coordinates: tuple[int, int], prompt: str, choice_list: list, player):
        """
        Initialize super class and the list of choices and consequences and the player.

        :param tuple coordinates: The location of the node. Other nodes can point to this node.
        :param str prompt: The prompt displayed to the user.
        :param list choice_list: A list of multiple choices and conditions as well as consequences of these choices.
        :param player: The player, for alternative choices and effects.
        """
        super().__init__(coordinates, prompt)  # Init StoryNode
        self.choice_list = choice_list  # Format of choice_list: [[answer, pointer],[answer, pointer],...]
        self.player = player

    def run(self):
        """
        Run and ask the player a question, returning a pointer to move to another node.

        :return: A coordinate of a pointer to another node.
        :rtype: tuple
        """
        # These are alternate options that are sometimes available to the player such as setting spawn or healing
        if self.player.beds_amount != 0:
            self.choice_list.append(['Use bed to set respawn point', self.coordinates])
        if self.player.raw_mutton_amount != 0 and self.player.health < 10:
            self.choice_list.append(['Consume raw mutton', self.coordinates])

        # Format of choice_list: [[answer, pointer],[answer, pointer],...]
        # Note: answer means the text that describes the choices

        invalid_response_message = 'Invalid Answer! Please enter the letter in front of the choice (e.g \"a\")'
        # To be displayed when the user enters an unrecognized response

        for line in self.prompt.split('~'):  # Use character '~' to represent a newline
            print(line)
            time.sleep(get_sleep_time(line))  # To create the effect of time flowing
        character_pointer_answer_list = []  # Format: [['a',pointer,answer],['b',pointer,answer],...]

        for i, choice in enumerate(self.choice_list):  # enumerate() starts at 0 and numbers the elements by increments of 1
            answer = choice[0]
            character_in_prompt = chr(i + 97)  # chr(97) = 'a', chr(98) = 'b', etc
            choices_prompt = character_in_prompt + '. ' + answer
            print(choices_prompt)
            character_pointer_answer_list.append([character_in_prompt, choice[1], choice[0]])  # Collect all the choices and characters into a single list
            # The character (like 'a', 'b', 'c', etc) are needed for checking for the player's responses

        while True:
            # Wait until the player gives a valid response
            player_response = input('Select an option: ').strip().strip('.').lower()  # To prevent additional characters and capitalization
            for character_pointer_answer in character_pointer_answer_list:  # Iterate through the choices
                if player_response == character_pointer_answer[0]:  # Check if player input matches the character
                    print('->', character_pointer_answer[2], '<-')  # Repeat the player's answers to them (not the letter/character, the answer)
                    # Check for special choices
                    if character_pointer_answer[2] == 'Use bed to set respawn point':
                        self.player.sleep(self.coordinates)
                    if character_pointer_answer[2] == 'Consume raw mutton':
                        self.player.eat_raw_mutton()
                    time.sleep(1)
                    return character_pointer_answer[1]  # Finally, return the corresponding pointer

            print(invalid_response_message)


class TextNode(StoryNode):
    """
    A type of node that prints some text, then returns a pointer to another node.

    Attributes:
    coordinates (tuple): The location of the node. Other nodes can point to this node.
    prompt (str): The prompt displayed to the user.
    pointer (tuple): The pointer to a node after printing the text.
    """

    def __init__(self, coordinates: tuple[int, int], prompt: str, pointer: tuple[int, int]):
        """
        Initialize super class and direct pointer.

        :param tuple coordinates: The location of the node. Other nodes can point to this node.
        :param str prompt: The prompt displayed to the user.
        :param tuple pointer: The pointer to a node after printing the text.
        """
        super().__init__(coordinates, prompt)
        self.pointer = pointer

    def run(self):
        """
        Run the node and print some text, then points to another node by returning a pointer.

        :return: A pointer to another node.
        :rtype: tuple
        """
        # Simply print the lines and return the pointer
        for line in self.prompt.split('~'):  # Use character '~' to represent a newline
            print(line)
            time.sleep(get_sleep_time(line))  # To create the effect of time flowing
        return self.pointer


class ConditionalNode:
    """
    A type of node that returns pointers depending on if a condition has been met.

    Attributes:
    coordinates (tuple): The location of the node. Other nodes can point to this node.
    prompt (str): The prompt displayed to the user.
    conditions_list (list): A list of conditions and their respective pointers.
    player: The player in case it needs to be used in the exec().
    """

    def __init__(self, coordinates: tuple[int, int], conditions_list: list, player = None):
        """
        Initialize super class and list of conditions and pointers and player.

        :param tuple coordinates: The location of the node. Other nodes can point to this node.
        :param list conditions_list: A list of conditions and their respective pointers.
        :param player: The player in case it needs to be used in the exec().
        """
        self.coordinates = coordinates
        self.conditions_list = conditions_list
        self.player = player

    def run(self):
        """
        Run the node and check for the conditions, returning a pointer to another node.

        :return: A pointer to another node.
        :rtype: tuple
        """
        # Use a global player variable for convenience


        # Format of conditions_list: [[condition (string), pointer],[condition (string), pointer]..]
        # The earlier a condition is in a list, the more it will be prioritized
        # There can only be one return pointer
        # Ex. player.coins = 6, player.health = 0
        # And the condition list is [['player.coins>=5', (5, 0)], ['player.health<=0', (5, 1)]]
        # Then the return pointer will be (5, 0)

        for condition_and_pointer in self.conditions_list:  # Iterate through all conditions and pointers in self.conditions_list
            try:
                if exec(condition_and_pointer[0]):  # Evaluate the condition
                    return condition_and_pointer[1]  # Return pointer
            except NameError:
                logging.error(f'Variable in condition {condition_and_pointer[0]} NOT ACCESSIBLE in node {self.coordinates}')
                sys.exit(1)
        logging.error(f'NO CONDITIONS WERE MET in node {self.coordinates}')
        sys.exit(1)


class EffectNode:
    """
    A type of node that changes some variable, returning a pointer to another node.

    Attributes:
    coordinates (tuple): The location of the node. Other nodes can point to this node.
    code (str): The code to execute.
    pointer (tuple): The pointer to a node after executing the code.
    player: The player in case it needs to be used in the exec().
    """

    def __init__(self, coordinates: tuple[int, int], code: str, pointer: tuple[int, int], player = None):
        """
        Initialize super class and direct pointer and player.

        :param tuple coordinates: The location of the node. Other nodes can point to this node.
        :param str code: The code to execute.
        :param tuple pointer: The pointer to a node after printing the text.
        :param player: The player in case it needs to be used in the exec().
        """
        self.coordinates = coordinates
        self.code = code
        self.pointer = pointer
        self.player = player

    def run(self):
        """
        Run the node and execute the code, returning a pointer to move on to another node.

        :return: A pointer to another node.
        :rtype: tuple
        """
        for line in self.code.split('~'):  # Use '~' as a newline indicator
            exec(line)  # Run the code
        return self.pointer
