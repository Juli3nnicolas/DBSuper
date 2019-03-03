class Card:
    def __init__(self):
        self._action = True
        self._color = "Blue"
        self._energy_cost = 1

    def can_be_set_to_action(self):
        return True
