
from classes import *

import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG)  # Change the level of the logger - logging.DEBUG for debug, logging.ERROR for error


player = Player()  # Will be used as a global variable for convenience

'''
# This storyline was too long and ambitious, and I also didn't know if the reader would enjoy such a long game.


# The full story in a single list
story_nodes_list = [
    # Organize using rows
    # Use character '~' to represent a newline
    [TextNode((0, 0), 'Laying in bed, you really don\'t want to wake up.~You overhear some chatter outside your open window.', (1, 0))],
    [TextNode((1, 0), '\"Have you heard? The prophecy?\"~\"Oh yeah, it goes something like this...\"~It catches your attention.', (2, 0))],
    [TextNode((2, 0), '\"Someday in the future, asteroids will rain down from the sky, and we will all be separated.\"', (3, 0))],
    [TextNode((3, 0), '\"Then, the world will perish in a giant collapse, leaving only the destined one alive crying alone.\"', (4, 0))],
    [TextNode((4, 0), '\"Pretty absurd, huh?\"~\"Yeah, well I don\'t really believe in it. Plus, what can we do even if it was true?\"', (5, 0))],
    [ChoiceNode((5, 0), 'You are curious and want to know more.', [['Shout from your window', (6, 0)], ['Go outside', (6, 1)]])],
    [TextNode((6, 0), '\"Hey! What\'s this prophecy about?!\" you shouted.~\"Who are you? And why are you screaming?!\" they replied.', (7, 0)), TextNode((6, 1), 'You walk outside and ask about the prophecy.', (7, 1))],
    [ChoiceNode((7, 0), 'It\'s probably a good idea to go outside instead.', [['Go outside.', (7, 2)], ['Go Outside!', (6, 1)]]), TextNode((7, 1), '\"Have you been eavesdropping on us?\"~\"Well, it\'s exactly as you heard. The prophecy says that asteroids will rain down from the sky, separating us, then collapse, leaving only the fated one alive, crying alone.\"', (8, 0))],
    [TextNode((8, 0), '\"If you\'re curious, you can try your luck asking around central Chronosia. That\'s where the prophecy came from, or so I\'ve heard\"', (9, 0))],
    [ChoiceNode((9, 0), '', [['Okay, thanks! I\'m heading there right now.', (10, 0)], ['Thanks, I\'ll do just that.', (10, 0)]])],
    [TextNode((10, 0), 'You walk towards the city center, until you see the massive Tower of Paradox, famous for it\'s studies on temporology (the study of time)', (11, 0))],
    [ChoiceNode((11, 0), 'There also seems to be a circle of people around something. ~A sign in front of you reads \"F8 -> Info about The Prophecy\".', [['Go to the 8th floor of the Tower of Paradox', (12, 0)], ['Walk towards the circle of people', (12, 1)]])],
    [TextNode((12, 0), 'You ride the elevator to the 8th floor of the Tower of Paradox. There is a small room right across with the sign \"The Temporal Organization of Chronosia (TTOC)\".', (13, 0))],
    [TextNode((13, 0), 'There are many items displayed around the room, like a museum. One particular set of objects interest you: the Temporal Shards', (14, 0))],
    [TextNode((14, 0), '\"Excavated in 2190, temporologists have been studying it\'s mysterious uses. They suggest that it may be capable of time travel.\"~\"Time travel?!\" you think. Time travel has always been one of your childhood dreams. And these glass shards may be capable of doing that?', (15, 0))],
    [ChoiceNode((15, 0), 'You look around and only see one guard, with no security cameras. Suddenly, you feel the urge to take the Temporal Shards for yourself', [['Go to the guard.', (16, 0)], ['Look for potential cracks in the case of the Temporal Shards', (16, 1)]])],
    [ChoiceNode((16, 0), 'You walk towards the guard. Several options appear in your mind. ', [['Attempt to bribe the guard', (17, 0)], ['Initiate small talk', (17, 1)]]), ChoiceNode((16, 1), 'You see that there are no screws in the glass box. Several options appear in your mind. ', [['Break the box with brute force', (17, 2)], ['Disassemble the box', (17, 3)], ['Take the entire box', (17, 4)]])]
]
'''

story_nodes_list = [
    # Organize using rows
    # Use character '~' to represent a newline
    # Minecraft story
    [TextNode((0, 0), 'You load a new game in Minecraft. In minecraft, your goal is to kill the Ender Dragon.', (1, 0))],
    [TextNode((1, 0), 'You spawn in a forest. This is great! It allows you to quickly obtain wood and food before monsters come out.', (2, 0))],
    [ChoiceNode((2, 0), 'You see some trees and some sheep. You only have limited time before enemies spawn!', [['Kill some sheep', (3, 1)], ['Mine some wood', (3, 0)]], player)],
    [EffectNode((3, 0), 'self.player.wood_amount += 2', (4, 0), player), EffectNode((3, 1), 'self.player.wool_amount += 3~self.player.raw_mutton_amount += 5', (4, 1), player)],
    [TextNode((4, 0), 'You got 2 pieces of wood!', (5, 0)), TextNode((4, 1), 'You got 5 raw button and 3 wool!', (5, 1))],
    [TextNode((5, 0), 'You decide it\'s probably a good idea to get a bit more wood and kill some sheep too.', (6, 0)), TextNode((5, 0), 'You decide it\'s probably a good idea to kill more sheep and get some wood too.', (6, 0))],
    [EffectNode((6, 0), 'self.player.wood_amount += 2~self.player.wool_amount += 3~self.player.raw_mutton_amount += 5', (7, 0), player)],
    [EffectNode((7, 0), 'print(f\"You now have {self.player.wood_amount} wood, {self.player.wool_amount} wool, and {self.player.raw_mutton_amount} raw mutton.\")', (8, 0), player)],
    []





]



# Start story on node (0, 0)
pointer = (0, 0)
logging.debug('GAME STARTED')
while True:
    logging.debug(f'Pointer at {pointer}')
    time.sleep(0.01)  # A short buffer time to ensure that the log prints before the node prints
    try:
        pointer = story_nodes_list[pointer[0]][pointer[1]].run()
    except IndexError:
        logging.error(f'Node at {pointer} cannot be located.')
        sys.exit(1)

'''
Peer reviews:

Name (relationship): "Feedback"

Response: Changes made to code

'''
