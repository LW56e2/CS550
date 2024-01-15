class Player:
    def __init__(self):
        self.wood_amount = 0
        self.wool_amount = 0
        self.raw_mutton_amount = 1
        self.beds_amount = 1
        self.health = 10
        self.respawn_node = (0, 0)
        self.potential_respawn_node = (0, 0)  # This is used for communication between ChoiceNode and EffectNode at row 0 if the player wants to set their spawn

    def sleep(self, coordinates):
        if self.beds_amount != 0:
            self.beds_amount -= 1
            print(f'Successfully set spawn. You now have {self.beds_amount} beds.')
            self.respawn_node = coordinates

    def eat_raw_mutton(self):
        self.raw_mutton_amount -= 1
        self.health += 1  # Heal the player
        print(f'You now have {self.raw_mutton_amount} raw mutton.')
        print(f'You are now at {self.health} health.')


