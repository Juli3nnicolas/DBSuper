from StateMachine import (StateMachine, Node)
import single_player_game_states as states


class SinglePlayerStateMachine(StateMachine):
    def __init__(self):
        super().__init__()

        # Define graph by instantiating game state
        self._active_node = Node(states.choose_first_player)


single_player_state_machine = SinglePlayerStateMachine()
