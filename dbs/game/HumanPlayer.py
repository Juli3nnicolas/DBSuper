NB_LIFE_POINTS = 8
NB_CARDS_IN_HAND_FIRST_TURN = 6
DECK_SIZE = 50


class HumanPlayer:
    def __init__(self):
        # A leader Card
        self._leader = ""
        # A list of DECK_SIZE Card s
        self._deck = list()
        for i in range(DECK_SIZE):
            self._deck.append(i)
        # A list of NB_CARDS_IN_HAND_FIRST_TURN -> nb cards to draw for the first turn
        self._hand = list()
        # A list of NB_LIFE_POINTS cards
        self._lp = list()
        pass

    def run(self):
        self.charging_phase()

    # Charging phase
    # :return: True if the phase could unfold without trouble, False if the player has lost (empty deck).
    def charging_phase(self):
        self.set_inertia_cards_to_action()
        if self.draw(1):
            self.play_charging_card()
            return True

        return False

    def set_inertia_cards_to_action(self):
        pass

    # Draw cards from the deck.
    # :return: True if all cards could be drawn, False if the deck is empty.
    def draw(self, nb_cards):
        for i in range(nb_cards):
            if len(self._deck) > 0:
                self._hand.append(self._deck.pop())
            else:
                return False

        return True

    def play_charging_card(self):
        pass

    # Main phase
    def main_phase(self):
        pass

    def play_card(self, card):
        pass

    def activate_effect(self, card):
        pass

    def _play_combat_card(self, combat):
        pass

    def _play_extra_card(self, extra):
        pass

    # End phase
    def end_phase(self):
        pass
