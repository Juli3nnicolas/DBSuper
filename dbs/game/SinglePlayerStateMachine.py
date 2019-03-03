from StateMachine import (StateMachine, Node, FINAL_NODE)
import single_player_game_states as states
import single_player_state_functions as func


class SinglePlayerStateMachine(StateMachine):
    def __init__(self):
        super().__init__()

        # Define graph by instantiating game state
        self._active_node = Node(states.choose_first_player)

        # Create game graph nodes
        player1_turn = Node(states.player1_turn)
        player2_turn = Node(states.player2_turn)
        end_of_game = Node(states.end_of_game)

        # Build the graph
        self._active_node.add_successor(player1_turn, func.transition_from_choose_first_player_to_p1_turn)
        self._active_node.add_successor(player2_turn, func.transition_from_choose_first_player_to_p2_turn)

        player1_turn.add_successor(player2_turn, func.transition_from_player1_turn_to_player2)
        player2_turn.add_successor(player1_turn, func.transition_from_player2_turn_to_player1)

        player1_turn.add_successor(end_of_game, func.transition_from_player1_turn_to_end_of_game)
        player2_turn.add_successor(end_of_game, func.transition_from_player2_turn_to_end_of_game)

        end_of_game.add_successor(FINAL_NODE, lambda: True)


single_player_state_machine = SinglePlayerStateMachine()
