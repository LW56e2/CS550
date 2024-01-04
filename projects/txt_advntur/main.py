"""
Name: Leo Wei
Date:
START - Dec 12th, 2023
END -

Sources: None

Reflection:

"""
from classes import *

import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG)  # Change the level of the logger - logging.DEBUG for debug, logging.ERROR for error


player = Player()  # Will be used as a global variable for convenience


# The full story in a single list
story_nodes_list = [
    # Organize using rows
    # Use character '~' to represent a newline
    [TextNode((0, 0), 'Laying in bed, you really don\'t want to wake up.~You overhear some chatter outside your open window.', (1, 0))],
    [TextNode((1, 0), '\"Have you heard? The prophecy?\"~\"Oh yeah, it goes like this...\"~It catches your attention.', (2, 0))],
    [TextNode((2, 0), '\"One day in the future, comets will rain down from the sky, and we will all be separated.\"', (3, 0))],
    [TextNode((3, 0), '\"Then, we will all be crushed together in a big collapse, leaving only the destined one alive\"', (4, 0))],
    [TextNode((4, 0), '\"Pretty absurd, huh?\"~\"Yeah, well its probably just some children\'s tales.\"', (5, 0))],
    [ChoiceNode((5, 0), 'You are curious and want to know more.', [['Shout from your window', (6, 0)], ['Go outside', (6, 1)]])],
    [TextNode((6, 0), '\"Hey! What\'s this prophecy about?!\" you shouted.~\"Who are you? And why are you screaming?!\" they replied.', (7, 0)), TextNode((6, 1), 'You walk outside and ask about the prophecy.', (7, 1))],
    [ChoiceNode((7, 0), 'It\'s probably a good idea to go outside instead.', [['Go outside.', (7, 2)], ['Go Outside!', (6, 1)]]), TextNode((7, 1), '\"Have you been eavesdropping on us?\"~\"Well, it\'s exactly as you heard. The prophecy says that comets will rain down from the sky, separating us, but we will then collapse into each other, leaving only the fated one alive.\"', (8, 0))],








]
# Start story on node (0, 0)
pointer = (0, 0)
logging.debug('GAME STARTED')
while True:
    logging.debug(f'Pointer at: {pointer}')
    time.sleep(0.01)  # A short buffer time to ensure that the log prints before the node prints
    try:
        pointer = story_nodes_list[pointer[0]][pointer[1]].run()
    except IndexError:
        logging.error(f'Node at {pointer} cannot be located.')
        sys.exit(1)
